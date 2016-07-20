@echo off
for /L %%v in (1, 1, 3) do (
	for %%i in (G:\TH14_Test_set_mp4\%%v\*.mp4) do (
		echo %%i
		Improved_Dense_Trajectories.exe %%i  -> G:\TH14_Test_set_mp4_Trajectories\%%v_%%~ni.txt
		)
	pause
)
echo on