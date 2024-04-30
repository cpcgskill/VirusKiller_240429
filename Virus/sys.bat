set uac=~uac_permission_tmp_%random%
            md "%SystemRoot%\system32\%uac%" 2>nul
            if %errorlevel%==0 ( rd "%SystemRoot%\system32\%uac%" >nul 2>nul ) else (
                echo set uac = CreateObject^("Shell.Application"^)>"%temp%\%uac%.vbs"
                echo uac.ShellExecute "%~s0","","","runas",1 >>"%temp%\%uac%.vbs"
                echo WScript.Quit >>"%temp%\%uac%.vbs"
                "%temp%\%uac%.vbs" /f
                del /f /q "%temp%\%uac%.vbs" & exit )
            reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" /v "ConsentPromptBehaviorAdmin" /t REG_DWORD /d 0 /f
            REG ADD HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v EnableLUA /t REG_DWORD /d 0 /f