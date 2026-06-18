[Setup]
AppName=tomd
AppVersion=1.2.6
AppPublisher=Ahmed Raouane
AppPublisherURL=https://github.com/ahmedRAOUANE/tomd
AppSupportURL=https://github.com/ahmedRAOUANE/tomd
AppUpdatesURL=https://github.com/ahmedRAOUANE/tomd
DefaultDirName={autopf}\tomd
DefaultGroupName=tomd
Compression=lzma
SolidCompression=yes
OutputDir=Output
OutputBaseFilename=tomd-setup

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Files]
Source: "dist\tomd\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

[Run]
Filename: "powershell.exe"; \
Parameters: "-NoProfile -ExecutionPolicy Bypass -Command ""$p = [Environment]::GetEnvironmentVariable('Path', 'User'); $app = '{app}'; if ($p -split ';' -notcontains $app) {{[Environment]::SetEnvironmentVariable('Path', $p + ';' + $app, 'User')}"""; \
Flags: runhidden

[UninstallRun]
Filename: "powershell.exe"; \
Parameters: "-NoProfile -ExecutionPolicy Bypass -Command ""$p = [Environment]::GetEnvironmentVariable('Path', 'User'); $app = '{app}'; $newPath = ($p -split ';' | Where-Object {{ $_ -ne $app }}) -join ';'; [Environment]::SetEnvironmentVariable('Path', $newPath, 'User')"""; \
Flags: runhidden; \
RunOnceId: "DelService"