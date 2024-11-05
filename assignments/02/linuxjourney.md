# Linux journey quiz documentation

## Questions

Q1: What should be outputted to the display when you type echo Hello World?                   
A1: Hello World

Q2: How do I find what directory you are currently in?                          
A2: ```pwd```

Q3: If you are in /home/pete/Pictures and wanted to go to /home/pete, what’s a good shortcut to use?   
A3: ```cd ..```

Q4: What command would you use to see hidden files?                                      
A4: ```ls -a```

Q5: How do you create a file called myfile?                                                      
A5: ```touch myfile```

Q6: What command can you use to find the file type of a file?                                     
A6: ```file```

Q7: What's a good way to see the contents of a file?                                               
A7: ```cat```

Q8: How do you quit out of a less command?                                                      
A8: ```q```

Q9: What is the command to clear the terminal?                                                     
A9: ```clear```  

Q10: What flag do you need to specify to copy over a directory?                                   
A10: ```-r```

Q11: How do you rename a file called cat to dog?                                                    
A11: ```mv cat dog```

Q12: What command is use to make a directory?                                                   
A12: ```mkdir```

Q13: How do you remove a file called myfile?                                                      
A13: ```rm myfile```

Q14: What option should I specify for find if I want to search by name?                           
A14: ```-name```

Q15: How do you get quick command line help for built-in bash commands?                               
A15: ```help```

Q15: How do you see the manuals for a command?                                                        
A15: ```man```

Q16: What command can you use to see a small description of a command?                               
A16: ```whatis```

Q18: What command is used to make an alias?                                                           
A18: ```alias```

Q19: How can you exit from the shell?                                                                
A19: ```  exit ```

## Output of the exercises

No.1: ```Wed Oct 30 12:03:15 CET 2024``` , ```leonthies```                                           
No.2: ```(base) leonthies@nat079026 ~ % ```                                                     
No.3:  ls -R: This command lists the contents of the current directory and all its subdirectories. It will show the files and directories in the current folder, and then for each subdirectory, it will recursively display its contents as well.     <br>                                              ls -r: This command lists the contents of the directory in reverse alphabetical order. <br>
ls -t: This command lists files sorted by the time they were last modified, with the most recently modified files appearing first. <br>
No.4: timestamp of newfile.txt : Wednesday, October 30, 2024 at 12:16 PM    <br> 
      timestamp after touching file: Wednesday, October 30, 2024 at 12:18 PM <br>
No.5: input: ```file newfile.txt``` output: ```empty```, <br> input: ```file X100V/```, output:```X100V: directory``` <br>
No.6: input: ```cat Downloads```output: ```cat: Downloads: Is a directory```,<br> input:```cat fileA.rtf```,  
output: ```{\rtf1\ansi\ansicpg1252\cocoartf2820
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0
\f0\fs24 \cf0 admasdmasmd}%```, <br> input: ```cat fileA.rtf FileB.rtf```, output: ```{\rtf1\ansi\ansicpg1252\cocoartf2820
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0
\f0\fs24 \cf0 admasdmasmd}{\rtf1\ansi\ansicpg1252\cocoartf2820
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0
\f0\fs24 \cf0 dadfasxxcc}%```





