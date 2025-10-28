Project Guide 
Installing FFmpeg and PortAudio 
Windows 
Download FFmpeg: 
     1.	Visit the official FFmpeg download page: FFmpeg Downloads 
     2.	Navigate to the Windows builds section and download the latest static build. 
Extract and Set Up FFmpeg: 
     1.	Extract the downloaded ZIP file to a folder (e.g., C:\ffmpeg). 
     2.	Add the bin directory to your system's PATH: 
      •	Search for "Environment Variables" in the Start menu. 
      •	Click on "Edit the system environment variables." 
      •	In the System Properties window, click on "Environment Variables." 
      •	Under "System variables," select the "Path" variable and click "Edit." 
      •	Click "New" and add the path to the bin directory (e.g., C:\ffmpeg\bin). 
      •	Click "OK" to apply the changes. 

Install PortAudio: 
  Download the PortAudio binaries from the official website:  PortAudio Downloads 
Setting Up a Python Virtual Environment: 
Using Pipenv 
1.Install Pipenv (if not already installed): 
   pip install pipenv 
2.Install Dependencies with Pipenv: 
   pipenv install 
3.Activate the Virtual Environment: 
   pipenv shell 

Using pip and venv 
Create a Virtual Environment: 
   python -m venv venv 
Activate the Virtual Environment: 
Windows: 
   venv\Scripts\activate 
Install Dependencies: 
   pip install -r requirements.txt 

Using Conda 
Create a Conda Environment: 
   conda create --name myenv python=3.11 
Activate the Conda Environment: 
   conda activate myenv 

Install Dependencies: 
pip install -r requirements.txt 
Project Phases and Python Commands 
  Phase 1: Brain of the doctor 
       python brain_of_the_doctor.py 
  Phase 2: Voice of the patient 
       python voice_of_the_patient.py 
  Phase 3: Voice of the doctor 
       python voice_of_the_doctor.py 
  Phase 4: Setup Gradio UI 
       python gradio_app.py
