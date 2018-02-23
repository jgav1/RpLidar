filename = 'Lidar 1.xlsx';
sheet = 6;
xlRange = 'C1:C81000';
x2Range = 'D1:D81000';
Angulo = xlsread(filename,sheet,xlRange)*pi/180
Radio = xlsread(filename,sheet,x2Range)
polarplot(Angulo,Radio,'*')
% 
% %%
% Angulo=[0,45,90,135,180,225,270,315,360]*pi/180
% Radio= [1,2^.5,1,2^.5,1,2^.5,1,2^.5,1]
% polarplot(Angulo,Radio,'*')