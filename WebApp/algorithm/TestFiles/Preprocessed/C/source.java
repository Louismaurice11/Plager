publicclassGFG{publicstaticvoidmain(String[]args)<missing ';'>{intnum=5;intx=0;for(inti=1;i<=num;i++){x=i-1;for(intj=i;j<=num-1;j++){System.out.print(" ");System.out.print("  ");}for(intj=0;j<=x;j++)System.out.print((i+j)<10?(i+j)+"  ":(i+j)+" ");for(intj=1;j<=x;j++)System.out.print((i+x-j)<10?(i+x-j)+"  ":(i+x-j)+" ");System.out.println();}}}