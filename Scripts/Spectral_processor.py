
'''
Making single SNAP object (or complex matrix Jones-based SNAP object) from the bunch of the files 
'''
__version__='2.6'
__date__='2023.01.19'

import os,sys
import numpy as np
import matplotlib.pyplot as plt
import time
from scipy import interpolate
from PyQt5.QtCore import QObject,pyqtSignal
import pickle
try:
    import Scripts.SNAP_experiment as SNAP_experiment
    import Scripts.OVA_signals as OVA_signals
except ModuleNotFoundError as E:
    print(E)
    os.chdir('..')
    # import Scripts.SNAP_experiment as SNAP_experiment
    # import Scripts.OVA_signals as OVA_signals
sys.modules['SNAP_experiment'] = SNAP_experiment

class Spectral_processor(QObject):
    S_print=pyqtSignal(str) # signal used to print into main text browser
    S_print_error=pyqtSignal(str) # signal used to print errors into main text browser

    def __init__(self, path_to_main:str):
        QObject.__init__(self)
        self.processedData_dir_path=path_to_main+'\\ProcessedData\\'
        self.source_dir_path=path_to_main+'\\SpectralData\\'
        self.use_out_of_contact_data=False  # do we use spectra measured out of contact with microcavity to extract those
        self.StepSize=30 # um, Step in Z direction, legacy code
        self.isAveraging=False 
        self.isShifting=False
        self.isInterpolation=True
        self.axis_to_plot_along='Z'
        self.type_of_input_data='pkl'
        self.file_naming_style='new' # legacy 
        self.type_of_output_data='SNAP'
        self.R_0=62.5
        self.refractive_index=1.45
        

    skip_Header=3

    number_of_axis={'X':0,'Y':1,'Z':2,'W':3,'p':4}
    AccuracyOfWavelength=0.008 # in nm. Maximum expected shift to define the correlation window

    Cmap='jet'
    
    def set_parameters(self,dictionary):
        for key in dictionary:
            try:
                self.__setattr__(key, dictionary[key])
            except:
                pass
                
    def get_parameters(self)->dict:
        '''
        Returns
        -------
        Seriazible attributes of the object
        '''
        d=dict(vars(self)) #make a copy of the vars dictionary
        return d
#
    def define_file_naming_style(self,FileName): # legacy code
        if FileName.find('X=')==-1:
            self.file_naming_style='old'
        else:
            self.file_naming_style='new'

    def find_between(self, s, first, last ): ## local function to find the substring between two given strings
        try:
            start = s.index( first ) + len( first )
            end = s.index( last, start )
            return s[start:end]
        except ValueError:
            return ""

    def get_min_max_wavelengths_from_file(self,file): # fastly extract min, maximum wavelength from the file
        def extract_wavelength_from_line(bytes_array):
            s=bytes_array.decode()
            a=s.find(' ')
            s=s[0:a]
            return float(s)
        
        if self.type_of_input_data=='txt':
            with open(file, "rb") as f:
                min_wavelength = extract_wavelength_from_line(f.readline())        # Read the first line.
                f.seek(-2, os.SEEK_END)     # Jump to the second last byte.
                while f.read(1) != b"\n":   # Until EOL is found...
                    f.seek(-2, os.SEEK_CUR) # ...jump back the read byte plus one more.
                max_wavelength = extract_wavelength_from_line(f.readline())         # Read last line.
            f.close()
            return min_wavelength,max_wavelength
        elif self.type_of_input_data=='pkl':
            Data=pickle.load(open(file,"rb"))
            return Data[0,0],Data[-1,0]
        
        elif self.type_of_input_data=='bin':
            OVA_signal = OVA_signals.load_OVA_spectrum(file)
            Wavelengths=OVA_signal.fetch_xaxis()[0]
            return Wavelengths[0],Wavelengths[-1]

    def get_position_from_file_name(self,string,axis): # extract postitions of the contact from the file name
        if self.file_naming_style=='old':
            string=string.split('_');
            return float(string[2])
        else:
            if axis=='X':
                return float(self.find_between(string,'X=','_Y'))
            if axis=='Y':
                return float(self.find_between(string,'Y=','_Z'))
            if axis=='Z':
                return float(self.find_between(string,'Z=','_.'))
            if axis=='W':
                try:
                    a=float(self.find_between(string,'W=','_'))
                except:
                    a=0
                return a
            if axis=='p':
                try:
                    a=int(self.find_between(string,'p=','_'))
                except:
                    a=0
                return a

    def Create2DListOfFiles(self,InputFileList,axis='X'):  
        '''
        Find all files which acqured at the same point
        
        return  structures file list and list of positions in microns!
        '''
        
        NewFileList=[]
        Positions=[]
        FileList=InputFileList.copy()
        ## if Files are named with X position then Using new
        if self.file_naming_style=='old':
            while FileList:
                Name=FileList[0]
                s=Name[:Name.rfind('_')+1]
                 #s=s[2] # take signature of the position,  etc
                Temp=[T for T in FileList if s in T]  # take all 'signature' + 'i' instances
                NewFileList.append(Temp)
                FileList=[T for T in FileList if not (T in Temp)]
            return NewFileList,Positions
        else:
        ## if Files are named with X position then Using new
            while FileList:
                Name=FileList[0]
                s=axis+'='+self.find_between(Name,axis+'=','_')
                # s=axis+'='+str(self.get_position_from_file_name(Name,axis=axis))+'_'
                 #s=s[2] # take signature of the position,  etc
                Temp=[T for T in FileList if s in T]  # take all 'signature' + 'i' instances
                NewFileList.append(Temp)
                Positions.append([self.get_position_from_file_name(Name,axis='X'),
                                  self.get_position_from_file_name(Name,axis='Y'),
                                  self.get_position_from_file_name(Name,axis='Z'),
                                  self.get_position_from_file_name(Name,axis='W'),
                                  self.get_position_from_file_name(Name,axis='p')])
                FileList=[T for T in FileList if not (T in Temp)]
            return NewFileList,Positions




    def InterpolateInDesiredPoint(self, YArray,XOldArray,XNewarray):
        f=interpolate.interp1d(XOldArray,YArray,bounds_error=False,fill_value=np.nan)
        Output=f(XNewarray)
        return Output

    def plot_sample_shape(self):
        from mpl_toolkits.mplot3d import Axes3D
        FileList=os.listdir(self.source_dir_path)
        if '.gitignore' in FileList:FileList.remove('.gitignore')
        FileList=sorted(FileList,key=lambda s:self.get_position_from_file_name(s,axis=self.axis_to_plot_along))
        StructuredFileList,Positions=self.Create2DListOfFiles(FileList,axis=self.axis_to_plot_along)
        Positions=np.array(Positions)
        plt.figure()
        ax = plt.axes(projection='3d')
        ax.plot(Positions[:,2],Positions[:,0],Positions[:,1])
        ax.set_xlabel('Z, microns')
        ax.set_ylabel('X, microns')
        ax.set_zlabel('Y, microns')
        plt.gca().invert_zaxis()
        plt.gca().invert_xaxis()




    def run(self):
        AccuracyOfWavelength=self.AccuracyOfWavelength
        time1=time.time()
        AllFilesList=os.listdir(self.source_dir_path)
        OutOfContactFileList=[]
        ContactFileList=[]
        if '.gitignore' in AllFilesList:AllFilesList.remove('.gitignore')
        '''
        Create list of files with spectra in contact 
        and list of files with spectra out of contact (if any)
        '''
        for file in AllFilesList:
           if self.type_of_input_data in file:
                if 'out_of_contact' in file and self.use_out_of_contact_data:
                    OutOfContactFileList.append(file)
                elif 'out_of_contact' not in file:
                    ContactFileList.append(file)
                    
        if len(ContactFileList)==0:
            self.S_print_error.emit('Error. No files found with specified parameters. Please recheck')

        '''
        legacy code
        Check if there are old measurements
        '''
        self.define_file_naming_style(ContactFileList[0])
        """
        group files at each point along microcavity
        """
        ContactFileList=sorted(ContactFileList,key=lambda s:self.get_position_from_file_name(s,axis=self.axis_to_plot_along))
        StructuredFileList,Positions=self.Create2DListOfFiles(ContactFileList,axis=self.axis_to_plot_along)
        NumberOfPointsZ=len(StructuredFileList)
        #Data = np.loadtxt(DirName+ '\\Signal' + '\\' +FileList[0])
        """
        Create main wavelength array
        """
        if self.type_of_input_data=='pkl':
            Wavelengths = pickle.load(open(self.source_dir_path +ContactFileList[0], "rb"))[:,0]
        elif self.type_of_input_data=='txt':
            Wavelengths=np.genfromtxt(self.source_dir_path +ContactFileList[0],skip_header=self.skip_Header)[:,0]
        elif self.type_of_input_data=='bin':
            OVA_signal = OVA_signals.load_OVA_spectrum(self.source_dir_path +ContactFileList[0])
            Wavelengths=OVA_signal.fetch_xaxis()[0]
            
        """
        interpolate a spectrum toward the unite wavelength grid  (Apex OSA, for instance, may change wavelength grid from a scan to scan)
        """
        if self.isInterpolation:
            MinWavelength,MaxWavelength=self.get_min_max_wavelengths_from_file(self.source_dir_path +ContactFileList[0])
            WavelengthStep=np.max(np.diff(Wavelengths))
            for File in ContactFileList:
                try:
                    minw,maxw=self.get_min_max_wavelengths_from_file(self.source_dir_path +File)
                except UnicodeDecodeError:
                    self.S_print_error.emit('Error while getting wavelengths from file {}'.format(File))
    
                if minw<MinWavelength:
                    MinWavelength=minw
                if maxw>MaxWavelength:
                    MaxWavelength=maxw
            MainWavelengths=np.arange(MinWavelength,MaxWavelength,WavelengthStep)
        else:
            MainWavelengths=Wavelengths
        NumberOfWavelengthPoints=len(MainWavelengths)
        SignalArray=np.zeros((NumberOfWavelengthPoints,NumberOfPointsZ))
        
        """
        Separate approaches for outputs with and without jones matrixes
        """    

        if self.type_of_output_data == 'cSNAP' : 
            if self.type_of_input_data=='bin':
                jones_matrixes_array=np.zeros((NumberOfWavelengthPoints,NumberOfPointsZ,2,2),dtype='complex_')
            else:
                self.S_print_error.emit('Error. input files should be processed as bin files to derive complex SNAP data.Please choose another output data type')
                return

        """
        Process files at each group
        Separate approaches for outputs with and without jones matrixes
        """

        for ii,FileNameListAtPoint in enumerate(StructuredFileList):
            NumberOfArraysToAverage=len(FileNameListAtPoint)
            SmallSignalArray=np.zeros((NumberOfWavelengthPoints,NumberOfArraysToAverage))
            ShiftIndexesMatrix=np.zeros((NumberOfArraysToAverage,NumberOfArraysToAverage))
            self.S_print.emit('{} {}'.format(ii,FileNameListAtPoint))
            
            """
            
            """
            if self.use_out_of_contact_data:
                for file in OutOfContactFileList:
                    OutOfContactFileName=''
                    if self.axis_to_plot_along+'='+self.find_between(FileNameListAtPoint[0],self.axis_to_plot_along+'=','_') in file:
                    # if self.axis_to_plot_along+'='+str(Positions[ii][self.number_of_axis[self.axis_to_plot_along]]) in file:
                        OutOfContactFileName=file
                        break
                try:
                    if self.type_of_input_data!='bin':
                        with open(self.source_dir_path +OutOfContactFileName,'rb') as f:
                            OutOfContactData=pickle.load(f)
                    
                        if self.isInterpolation:
                            OutOfContactSignal=self.InterpolateInDesiredPoint(OutOfContactData[:,1],OutOfContactData[:,0],MainWavelengths)
                        else:
                            OutOfContactSignal=OutOfContactData[:,1]
                    elif self.type_of_input_data == 'bin' :
                        OVA_signal_out_of_contact = OVA_signals.load_OVA_spectrum(self.source_dir_path +OutOfContactFileName)
                        jones_matrixes_out_of_contact=np.array(OVA_signal_out_of_contact.jones_matrixes)  
                except:
                    OutOfContactSignal=np.zeros((1,NumberOfWavelengthPoints))
                    print('out of contact file {} is not found'.format(OutOfContactFileName))

       
       
            for jj, FileName in enumerate(FileNameListAtPoint):
                try:
                    if self.type_of_input_data=='pkl':
                        Data = pickle.load(open(self.source_dir_path +FileName, "rb"))
                        signal=Data[:,1]
                        wavelengths=Data[:,0]
                    elif self.type_of_input_data=='txt':
                        Data = np.genfromtxt(self.source_dir_path +FileName,skip_header=self.skip_Header)
                        signal=Data[:,1]
                        wavelengths=Data[:,0]
                    elif self.type_of_input_data=='bin':
                            OVA_signal = OVA_signals.load_OVA_spectrum(self.source_dir_path +FileName)
                            jones_matrixes=np.array(OVA_signal.jones_matrixes)
                            wavelengths=OVA_signal.fetch_xaxis()[0]
                            if self.use_out_of_contact_data:
                                jones_matrixes=SNAP_experiment.extract_taper_jones_matrixes(jones_matrixes,jones_matrixes_out_of_contact)
                                signal=(abs(jones_matrixes[:,0,0])**2+abs(jones_matrixes[:,0,0])**2)/2
                            else:
                                signal=OVA_signal.IL()
                                
                                
                except UnicodeDecodeError:
                    print('Error while getting data from file {}'.format(FileName))
                if self.isInterpolation:
                    SmallSignalArray[:,jj]=self.InterpolateInDesiredPoint(signal,wavelengths,MainWavelengths)
                else:
                    SmallSignalArray[:,jj]=np.array(signal,ndmin=1)
                if self.use_out_of_contact_data and self.type_of_input_data!='bin':
                    SmallSignalArray[:,jj]-=np.array(OutOfContactSignal,ndmin=1)

          
            '''
            Averaging spectra measured at the same point
            OR
            Calculate cross correlation between spectra measured at the same point
            do no work with 'bin' Luna data (for the sake of speed)
            '''
            if self.isAveraging or self.isShifting:
                SignalLog=np.zeros(NumberOfWavelengthPoints)
                MeanLevel=np.mean(SmallSignalArray)
                ShiftArray=np.zeros(NumberOfArraysToAverage)
                if self.isShifting:
                    """
                    Apply cross-correlation for more accurate absolute wavelength determination
                    """
                    for jj, FileName in enumerate(FileNameListAtPoint):
                        for kk, FileName in enumerate(FileNameListAtPoint):
                            if jj<kk:
                                Temp=np.correlate(SmallSignalArray[int(AccuracyOfWavelength/WavelengthStep):-int(AccuracyOfWavelength/WavelengthStep),kk],SmallSignalArray[:,jj], mode='valid')/ \
                                    np.sum(SmallSignalArray[int(AccuracyOfWavelength/WavelengthStep):-int(AccuracyOfWavelength/WavelengthStep),jj]**2)
                                ShiftIndexesMatrix[jj,kk]=np.nanargmax(Temp)-np.floor(AccuracyOfWavelength/WavelengthStep)
                                ShiftIndexesMatrix[kk,jj]=-ShiftIndexesMatrix[jj,kk]
                    ShiftArray=(np.mean(ShiftIndexesMatrix,1))
                   
                if self.isAveraging:
                    """
                    Apply self.isAveraging across the spectra at one point
                    """
                    for jj, FileName in enumerate(FileNameListAtPoint):
                        Temp=np.ones(NumberOfWavelengthPoints)*MeanLevel
                        Temp[int(AccuracyOfWavelength/WavelengthStep)+int(ShiftArray[jj]):-int(AccuracyOfWavelength/WavelengthStep)+int(ShiftArray[jj])]=SmallSignalArray[int(AccuracyOfWavelength/WavelengthStep):-int(AccuracyOfWavelength/WavelengthStep),jj]
                        SignalLog+=Temp
                    SignalArray[:,ii]=SignalLog/NumberOfArraysToAverage#-np.nanmax(SignalLog)
                elif self.isShifting:
                    Temp=np.ones(NumberOfWavelengthPoints)*MeanLevel
                    Temp[int(AccuracyOfWavelength/WavelengthStep)+int(ShiftArray[0]):-int(AccuracyOfWavelength/WavelengthStep)+int(ShiftArray[0])]=SmallSignalArray[int(AccuracyOfWavelength/WavelengthStep):-int(AccuracyOfWavelength/WavelengthStep),0]
                    SignalArray[:,ii]=Temp
                    
            else:
                """
                    If self.isShifting and self.isAveraging are OFF, just take the first spectrum from the bundle correpsonding to a measuring point
                """
                SignalArray[:,ii]=SmallSignalArray[:,0]
                if self.type_of_output_data == 'cSNAP': 
                    jones_matrixes_array[:,ii,:,:]=jones_matrixes

        if self.axis_to_plot_along=='W':
            self.f_name='Processed_spectra_VS_wavelength.'+self.type_of_output_data     
        elif self.axis_to_plot_along=='p':
            self.f_name='Processed_spectrogram_at_spot.'+self.type_of_output_data         
        else:
            self.f_name='Processed_spectrogram.'+self.type_of_output_data         
        from datetime import datetime
       
        if self.type_of_output_data in ['cSNAP','SNAP']:
            if self.type_of_output_data=='cSNAP':
                SNAP=SNAP_experiment.SNAP(jones_matrixes_used=True)
                SNAP.jones_matrixes_array=jones_matrixes_array
            else:
                SNAP=SNAP_experiment.SNAP(jones_matrixes_used=False)
            SNAP.date=datetime.today().strftime('%Y.%m.%d')
            SNAP.positions=np.array(Positions)
            SNAP.wavelengths=MainWavelengths
            SNAP.signal=SignalArray
            SNAP.type_of_signal='insertion losses'
            SNAP.axis_key=self.axis_to_plot_along
            SNAP.lambda_0=min(MainWavelengths)
            SNAP.R_0=self.R_0
            SNAP.refractive_index=self.refractive_index
            f=open(self.processedData_dir_path+self.f_name,'wb')
            pickle.dump(SNAP,f)
            f.close()
            print('Spectrogram saved as SNAP object to {}'.format(self.processedData_dir_path+self.f_name))                 

        elif  self.type_of_output_data=='pkl3d':
            f=open(self.processedData_dir_path+self.f_name,'wb')
            D={}
            D['axis']=self.axis_to_plot_along
            D['spatial_scale']='microns'
            D['Positions']=np.array(Positions)
            D['Wavelengths']=MainWavelengths
            D['Signal']=SignalArray
            D['R_0']=self.R_0
            D['type_of_signal']='insertion losses'
            D['refractive_index']=self.refractive_index
            from datetime import datetime
            D['date']=datetime.today().strftime('%Y.%m.%d')
        
            pickle.dump(D,f)
            f.close()
            print('Spectrogram saved as pkl3d file to {}'.format(self.processedData_dir_path+self.f_name))

        if self.file_naming_style=='old': # legacy code, to save in txt format
            
            X_0=0
            X_max=self.StepSize*NumberOfPointsZ
            # plt.figure()# 
            # plt.imshow(SignalArray, interpolation = 'bilinear',aspect='auto',cmap=self.Cmap,extent=[X_0,X_max,MainWavelengths[0],MainWavelengths[-1]],origin='lower')# vmax=0, vmin=-1)
            # plt.show()
            # plt.colorbar()
            # plt.xlabel(r'Position, steps (2.5 $\mu$m each)')
            # plt.ylabel('Wavelength, nm')
            # ax2=(plt.gca()).twiny()
            # ax2.set_xlabel(r'Distance, $\mu$m')
            # ax2.set_xlim([0,self.StepSize*NumberOfPointsZ*2.5])
            # plt.tight_layout()
            # plt.savefig(self.processedData_dir_path+'Scanned WGM spectra')
            Positions=[np.linspace(0, self.StepSize*NumberOfPointsZ,NumberOfPointsZ),np.linspace(0, self.StepSize*NumberOfPointsZ,NumberOfPointsZ),np.linspace(0, self.StepSize*NumberOfPointsZ,NumberOfPointsZ)]
            Positions=np.transpose(Positions)
            np.savetxt(self.processedData_dir_path+'Sp_Positions.txt', Positions)

        # if self.file_naming_style=='new':
            
        #     Positions_at_given_axis=np.array([s[self.number_of_axis[self.axis_to_plot_along]] for s in Positions])
        #     plt.figure()
        #     try:
        #         plt.pcolorfast(Positions_at_given_axis,MainWavelengths,SignalArray,cmap=self.Cmap)
        #     except:
        #         plt.contourf(Positions_at_given_axis,MainWavelengths,SignalArray,50,cmap=self.Cmap)
        #     plt.gca().pcolorfast(Positions_at_given_axis,MainWavelengths,SignalArray)
        #     plt.ylabel('Wavelength, nm')
        #     if self.axis_to_plot_along=='W':
        #         plt.xlabel('Wavelength,nm')
        #     else:
        #         plt.xlabel(r'Distance, $\mu$m')

                
        #     plt.colorbar()
        #     plt.tight_layout()
        #     plt.savefig(self.processedData_dir_path+'Scanned WGM spectra')
        #     time2=time.time()
        # print('Time used =', time2-time1 ,' s')

if __name__ == "__main__":
    # os.chdir('..')
    # path= os.getcwd()
    path='C:\\Users\\t-vatniki\\Desktop\\SpectralData'
    p=Spectral_processor(path)
    p.type_of_input_data='pkl'
    p.isInterpolation=False
    p.axis_to_plot_along='Z'
    p.type_of_output_data='SNAP'
    p.source_dir_path=path+'\\'
    p.processedData_dir_path=path+'\\'
    p.use_out_of_contact_data=True
    p.run()
# 
    # p.run()