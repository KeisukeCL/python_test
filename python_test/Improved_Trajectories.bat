@echo off

for /L %%i in (1, 1, 1574) do (
	mkdir G:\TH14_Test_set_mp4_Trajectories\%%i
	for /D in ()
	Improved_Dense_Trajectories G:\TH14_Test_set_mp4\%%i\%%i.mp4 -> G:\TH14_Test_set_mp4_Trajectories\%%i\%%i_%%i.txt
)

echo on