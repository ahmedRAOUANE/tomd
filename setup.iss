#define MyAppName "tomd"
#define MyAppVersion "1.0.1"
#define MyAppPublisher "ahmed"
#define MyAppURL ""
#define MyAppExeName "tomd.exe"
#define MyAppAssocName MyAppName + " File"
#define MyAppAssocKey StringChange(MyAppAssocName, " ", "")

[Setup]
AppId={{50E7B0A0-3934-4823-A0CE-366F4A121AAD}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={autopf}\{#MyAppName}
UninstallDisplayIcon={app}\{#MyAppExeName}
ArchitecturesAllowed=x64compatible
ArchitecturesInstallIn64BitMode=x64compatible
ChangesAssociations=yes
DisableProgramGroupPage=yes
PrivilegesRequired=lowest
OutputBaseFilename=tomd_setup
SolidCompression=yes
WizardStyle=modern dynamic

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Files]
Source: "dist\{#MyAppExeName}"; DestDir: "{app}"; Flags: ignoreversion;

[Run]
Filename: "powershell.exe"; \
Parameters: "-NoProfile -ExecutionPolicy Bypass -Command ""$p = [Environment]::GetEnvironmentVariable('Path', 'User'); $app = '{app}'; if ($p -split ';' -notcontains $app) {{[Environment]::SetEnvironmentVariable('Path', $p + ';' + $app, 'User')}"""; \
Flags: runhidden

[UninstallRun]
Filename: "powershell.exe"; \
Parameters: "-NoProfile -ExecutionPolicy Bypass -Command ""$p = [Environment]::GetEnvironmentVariable('Path', 'User'); $app = '{app}'; $newPath = ($p -split ';' | Where-Object {{ $_ -ne $app }}) -join ';'; [Environment]::SetEnvironmentVariable('Path', $newPath, 'User')"""; \
Flags: runhidden; \
RunOnceId: "DelService"
