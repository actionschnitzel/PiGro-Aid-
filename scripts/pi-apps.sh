$DESKTOP_SESSION=xfce

   # Existiert die Datei oder ist sie nur nicht lesbar? 
   if $DESKTOP_SESSION=TRUE
   then
     
     sudo thunar
             
   else
     sudo pcmanfm
     
   fi
 fi