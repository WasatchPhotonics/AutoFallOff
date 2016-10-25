; See the file py2exe_applicatin.py for details on how to create a
; windows installer
;
; Redefine these for the application to be built
#define MyAppName "AutoFallOff"
#define module_name "autofalloff"
#define MyAppExeName "AutoFallOff.exe"
;
;
; Built for InnoSetup version 5.5.6 on Windows 7 x64
;
;
; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

; Auto Versioning section
; Read the previous build number. If there is none take 0
#define BuildNum Int(ReadIni(SourcePath + "\\BuildInfo.ini","Info","Build","0"))

; Increment the build number by one
#expr BuildNum = BuildNum + 1

; Store the number in the ini file for the next build.
#expr WriteIni(SourcePath + "\\BuildInfo.ini","Info","Build",BuildNum)


#define MyAppPublisher "Wasatch Photonics"
#define MyAppURL "http://wasatchphotonics.com"

[Setup]
; NOTE: The value of AppId uniquely identifies this application.
; Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{B9977C21-3BA0-4CCB-8398-0A87B23BB849}

; See auto versioning section above
; Make the major version bumps manual here and have the command line
; builds part of the auto-increment
AppVersion=0.1.{#BuildNum}

AppName={#MyAppName}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={pf}\{#MyAppName}
DisableDirPage=yes
DefaultGroupName={#MyAppName}
OutputDir=windows_installer
OutputBaseFilename={#MyAppName}_setup
Compression=lzma
SolidCompression=yes
SetupIconFile=..\{#module_name}\assets\images\ApplicationIcon.ico
UninstallDisplayIcon={app}\{#MyAppExeName}

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
; "Regular" files
Source: "built-dist\*"; DestDir: "{app}"; Flags: recursesubdirs ignoreversion

; Required mkl_avx.dll file - note how brittle this is. Really should
; find out why the pyinstaller does not seem to include this.
; For appveyor:
 Source: "C:\Miniconda\envs\autofalloff_conda\Library\bin\mkl_avx.dll"; DestDir: "{app}\autofalloff\"; Flags: recursesubdirs ignoreversion

; Yes, it must be from appveyor and not from the local respository, as
; the architectures appear different. The msvcr100.dll file apparently
; does not have this issue.


; Source: "vcredist_x86.exe"; DestDir: {tmp}; Flags: deleteafterinstall


; There are many ways to include a Visual Studio runtime distributable. This way is to copy the dll into the application folder.
Source: "support_files\msvcr100.dll"; DestDir: "{app}\autofalloff\"; Flags: recursesubdirs ignoreversion


; Simulation imagery
Source: "..\autofalloff\assets\example_data\*"; DestDir: "{app}\autofalloff\autofalloff\assets\example_data"; Flags: recursesubdirs ignoreversion 


[Icons]
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppName}\{#MyAppExeName}"; IconFilename: "{app}\{#MyAppName}\{#MyAppExeName}"
Name: "{commondesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppName}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
; See notes above for why this is commented out:
; Filename: {tmp}\vcredist_x86.exe; Parameters: "/q /passive /Q:a /c:""msiexec /q /i vcredist.msi"" "; StatusMsg: Installing VC++ 2010 Redistributables...

Filename: "{app}\{#MyAppName}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent
