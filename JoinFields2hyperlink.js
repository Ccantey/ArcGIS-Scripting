//hyperlink JavaScript with ArcGIS 

//example data

//ObjectID   //Path                 //Attachment
//001        //C://users/gis/       //1094.pdf
//002        //C://users/gis/       //1095.pdf
//003        //C://users/gis/       //1096.pdf
//004        //C://users/gis/       //1099.pdf
//005        //C://users/gis/       //1456.pdf
//006        //C://users/gis/       //2354-1.pdf

// Layer Properties/Display tab
// "Support Hyperlinks using field: Script-> Edit -> Parser: JScript

function OpenLink ( [Path] , [Attachment]  )
{
  var objShell = new ActiveXObject("Shell.Application");
  var path = [Path] + [Attachment] ;
  objShell.ShellExecute(path, "", "", "open", 1);
}
