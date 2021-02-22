% Foerst importerer du doedssannsynlighetene.
% Du gjoer det ved aa (instruksjonene er testet paa pc):
%  1) Laste ned filen "doedelighet-felles.txt" fra kurssiden
%  2) Klikke paa "Import Data" i MATLAB
%  3) Velge filen "doedelighet-felles.txt" 
%  4) Klikke paa "Import Selection" 
%     (importer dataene som "Column vectors")
% Merk at paa filen er doedssannsynlighetene gitt i promille.
%% 
 
% Beregner ettaarige doedssannsynligheter:
qx=dod/1000;
%% 
 
% Beregner kumulativ fordeling for gjenstaaende levetid X:
Fx=1-cumprod(1-qx(31:107));
%% 
 
% Plotter den kumulative fordelingen:
stairs(0:76,Fx)
xlabel('Gjenstående levetid')
title('Kumulativ fordeling')
%% 
 
% Beregner punktsannsynlighetene for X:
px=Fx-[0;Fx(1:76)];
%% 
 
% Plotter punktsannsynlighetene:
bar(0:76,px)
xlabel('Gjenstående levetid')
title('Punktsannsynlighet')
%% 
 
% Beregner forventet naaverdi av erstatningsutbetalingene
% Merk at vi definerer vektorene som søylevektorer (slik at de har samme
% dimensjon som vektoren av dødssannsynligheter)
x=(0:76)'
hx=(1000000./1.03.^x).*(x<=34)
EhX=sum(hx.*px)
%% 
 
% Beregner forventet nåverdi av premieinnbetalingne pr krone (dvs for K=1):
gx=(1-(1/1.03).^(min(x,34)+1))/(1-(1/1.03))
EgX=sum(gx.*px)
%% 
 
% Beregner premien:
premie=EhX/EgX
