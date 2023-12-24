 var startval=1;
 var dict2 = {};
 var dict1 = {};
      
    var endval = 3;
    var date = new Date();
	  var current_date =date.getDate()+"-"+(date.getMonth()+1)+"-"+ date.getFullYear();
    var navButtons = document.getElementById("nav-buttons");
    var present = document.getElementById("present");
    var absent = document.getElementById("absent");
    var head1 = document.getElementById("head1");
    var head2 = document.getElementById("head2");
    var li = document.getElementById("list1");
    var li2 = document.getElementById("list2");
    var allmembers = document.getElementById("allmembers");
    const copybtn=document.getElementById("copybtn");
    const sharebtn=document.getElementById("sharebtn");
    const sharebtn2=document.getElementById("sharebtn2");
    const copybtn2=document.getElementById("copybtn2");
    const changeformate=document.getElementById("changeformate");
    const editformate=document.getElementById("editformate");
    const form1=document.getElementById("form1");
    const texter=document.getElementById("texter");
    const texter2=document.getElementById("texter2");
    const date1=document.getElementById("date");
    const date2=document.getElementById("date1");
    const submitbtn=document.getElementById("submitbtn");
    const databtn=document.getElementById("databtn");
    const savepoint=document.getElementById("savepoint");
    const cleardatabase=document.getElementById("cleardatabase");
    var mylist = document.getElementById("myList");
    var whatsapp = document.getElementById("whatsapp");
     var str1="5"
    var notli=[10]
    notli.sort(function(a, b){return a-b});
    var deli=[]
    var feli=[]
    var all_li=[]
    let myDataBase = []
    let myDataBase2 = []
    const dataBaseFromLocalStorage = JSON.parse(localStorage.getItem("myDataBase"))
    const dataBaseFromLocalStorage2 = JSON.parse(localStorage.getItem("myDataBase2"))
    var bool = 0
    if (dataBaseFromLocalStorage) {
        myDataBase = dataBaseFromLocalStorage
        myDataBase2 = dataBaseFromLocalStorage2
        render(myDataBase,myDataBase2)
    }
    sharebtn.addEventListener('click', function(event) {
      var ff="CSE-A  "+current_date+"%0A" +head1.innerHTML.slice(0,7).trim()+"ees:%0A"+li.innerHTML
      whatsapp.setAttribute("href","https://api.whatsapp.com/send/?text="+ff);
      whatsapp.click();
    });
    sharebtn2.addEventListener('click', function(event) {
      var ff="CSE-A %20"+current_date+"%0A"+head2.innerHTML.slice(0,7).trim()+"ees"+":%0A"+li2.innerHTML;
      console.log(ff);
      whatsapp.setAttribute("href","https://api.whatsapp.com/send/?text="+ff);
     whatsapp.click();
    });
    copybtn.addEventListener('click', function(event) {
      navigator.clipboard.writeText("\nCSE-A   "+head1.innerHTML.slice(0,21)+" :   "+li.innerHTML);
    });
    copybtn2.addEventListener('click', function(event) {
      navigator.clipboard.writeText("\nCSE-A  "+head2.innerHTML.slice(0,21)+" :    "+li2.innerHTML);
    });
    texter.addEventListener('change', function (event) {
      console.log(texter.value);
    });
    function setter(){
    var button = document.createElement("button");
    button.setAttribute("id", "order1");
    button.setAttribute("style", "display:none;");
    button.innerHTML=" sort it "
    head1.innerText+="     "+current_date+"  ";
    head1.appendChild(button);
    // date1.innerText=current_date;
    head2.innerHTML+="     "+current_date+"  ";
    var button1 = document.createElement("button");
    button1.innerHTML="      sort it "
    button1.setAttribute("id", "order2");
    button1.setAttribute("style", "display:none;");
    head2.appendChild(button1);
    // date2.innerHTML="    "+current_date+"    ";
    };
    setter();
    changeformate.onclick=function (){
      if (allmembers.className=="mark1"){
        allmembers.className="mark"
      }else{
        allmembers.className="mark1"
      }
      // console.log(allmembers.className);
      var mk1=present.className
      var mk2=absent.className
      present.setAttribute("class",mk2);
      absent.setAttribute("class",mk1);
      var mk1=head1.innerHTML
      head1.innerHTML=head2.innerHTML;
      head2.innerHTML=mk1;
    };
    var order1 = document.getElementById("order1");
    var order2 = document.getElementById("order2");
    order1.onclick=function (){
      //var dict1 = {};
      for(i=0;i<present.children.length;i++){
        var ff=present.children[i];
        var f2=parseInt( present.children[i].id.slice(6));
        dict1[f2]=ff;
      }
      present.innerHTML=""
      present.appendChild(head1)
      for(i=0;i<deli.length;i++){
        present.appendChild(dict1[deli[i]])
      }
    };
    order2.onclick=function (){
      //var dict2 = {};
      for(i=1;i<absent.children.length;i++){
        var ff=absent.children[i];
        var f2=parseInt( absent.children[i].id);
        // console.log(absent.children[i],f2);
        dict2[f2]=ff;
      }
      // console.log(dict2);
      absent.innerHTML=""
      absent.appendChild(head2)
      for(i=0;i<feli.length;i++){
        absent.appendChild(dict2[feli[i]])
      }
    };
    editformate.onclick=function (){
      if (form1.style.display === "none") {
        form1.style.display = "block";
      } else {
        form1.style.display = "none";
      }
    };
    submitbtn.onclick=function(){
          var formstart=document.getElementById("startnumber");
          var formend=document.getElementById("endnumber");
          var temp,sm,lg;
          if(formend.value==""){
            sm=1;
          }else{
            sm=parseInt(formend.value);
          }
          if(formstart.value==""){
            lg=13;
          }else{
            lg=parseInt(formstart.value);
          }
          if (sm>lg){
            temp=sm;
            sm=lg;
            lg=temp;
          }
          startval=sm;
          endval=lg;
          fun2();
          
    };
    function triggerfun(){
      console.log(mylist.options[mylist.selectedIndex].text)
      switch (mylist.options[mylist.selectedIndex].text) {
        case "only numbers":
        console.log("---------");
          break;
        case "only unit place digit":
          break;
        case "hexa decimal value":
          break;
        case "college attendence number":
          break;
        case "--custom--":
          break;
      }
    };
    function fun4(k1,k2){
      startval=k1;
      endval=k2;
      all_li=[];
      fun2();
    };
    function render(leads,leads2) {
      let listItems = ""
      // class="btn btn-primary"
      for (let i = 0; i < leads.length; i++) {
          listItems += `
          <button class="btn btn-primary m-2 step1" onclick="fun4(${leads[i]},${leads2[i]})">sta=${leads[i]}  end=${leads2[i]}</button>
          `
      }
      databtn.innerHTML = listItems
    };
    savepoint.addEventListener("click", function() {
      all_li=[]    
      submitbtn.click()
          var flag=0
          if(myDataBase.includes(startval) && myDataBase2.includes(endval))
          {
            var li=getInd(myDataBase,startval)
            for(i=0;i<li.length;i++){
              if(myDataBase2[li[i]]==endval)
                flag+=1
            }
          }

          if(flag===0){
          myDataBase.push(startval)
          myDataBase2.push(endval)
          localStorage.setItem("myDataBase", JSON.stringify(myDataBase))
          localStorage.setItem("myDataBase2", JSON.stringify(myDataBase2))
          render(myDataBase,myDataBase2)
          }
    });
    cleardatabase.addEventListener("click", function() {
      if(confirm("Need to clear all data from database.")){
      localStorage.clear()
      myDataBase = []
      myDataBase2 = []
      render(myDataBase,myDataBase2)
      }
    });
    function fun3(){
      if(deli.length>0){
      li.innerHTML=deli[0];
      for (i=1;i<deli.length;i++)
      li.innerHTML=li.innerHTML+" , "+deli[i];
    }
    else li.innerHTML="";
    texter.setAttribute('value',li.innerHTML);
    if(feli.length>0){
     li2.innerHTML=feli[0];
     for (i=1;i<feli.length;i++)
     li2.innerHTML=li2.innerHTML+" , "+feli[i];
    }
    else li2.innerHTML="";
    texter2.setAttribute('value',li2.innerHTML);
    fun5();
    }; 
    function getInd(arr, val) {
      var index = [], i = -1;
      while ((i = arr.indexOf(val, i+1)) != -1){
          index.push(i);
      }
      return index;
  };     
  function remove_ele(arr,value) {
    return arr.filter(function(ele){ 
      return ele != value; 
  });
  };
    function fun1(){
      feli=[]
      deli=[]
    for (i=startval;i<endval+1;i++)
      {
        if (!notli.includes(i)){
          deli.push(i);
          all_li.push(i);}
      }
      //console.log(all_li);
    };
  function fun5() {
    
    allmembers.innerHTML=""
    console.log(  );
    order1.click()
    order2.click()
    // console.log("@@@",dict1,"\n1",deli,dict2,"\n2",feli,all_li);
    // console.log(startval,'==',endval );
    // var j=startval+all_li.length+no_of_ele(notli.length,startval,endval);
    // console.log(startval,all_li.length,notli.length,j);
    // if (endval>notli.length);
    // else j=startval+all_li.length;
    var cc2="<h1>hello</h1>";
    // console.log(all_li);
    // console.log(i,"\n-->>");
    for(it=0;it<all_li.length;it++){
      i=all_li[it]
      if (deli.includes(i)){
        // console.log(dict1[i],"jklkjhjk");
        // var x1=dict1[i].innerText
        // var x2=dict1[i]

        // if (x1==501){
        //   console.log(dict1[i]);
        //   x2.setAttribute("class","ddd");
        //   console.log(dict1[i]);
        // }
//         x1.setAttribute("class","ddd")
//         var x2=dict1[i]
// console.log("////////////////////////////////",x2,x1);
      allmembers.appendChild(dict1[i]);
    }
      else{
        // console.log("----------------------------",i);
        allmembers.appendChild(dict2[i]);
      }
    }
    // console.log(head1.innerHTML.slice(0,21));
    // var cc2="<h1>hello</h1>"
    // allmembers.appendChild(cc2);
    // for (i=0;i<all_li.length;i++){
    //   var button = document.createElement("button");
    //   if(deli.includes(all_li[i])){
    //       button.setAttribute("class", "v1 roll");
    //     }
    //   else{
    //     button.setAttribute("class", "v2 roll");
    //   }
    //   var tenthpla="";
    //   if (all_li[i]<10) {
    //     tenthpla="0"
    //   }
    //   button.innerHTML=str1+tenthpla + all_li[i];
    //   allmembers.appendChild(button);
    // }

  }
  function fun2(){
    fun1();
    console.log("sm",startval,"en",endval)
    
      present.innerText="";
    for (var b=0; b<deli.length;b++)
    {  
      // btn btn-info link-success btn-lg
      // btn btn-info link-danger btn-lg
          var button = document.createElement("button");
          button.setAttribute("class", "btn btn-success m-3 p-6  btn-lg mybtn");
          // head1.innerText+=deli.length;
          
          // btn.setAttribute("type", "button");
          // button.setAttribute("class", "roll1");
          button.setAttribute("id", "temp__"+deli[b]);
          button.setAttribute("onClcik","fun1(this.id)" );
          var tenthpla="";
          if (deli[b]<10) {
            tenthpla="0"
          }
          button.innerHTML=str1+tenthpla + deli[b];
          present.appendChild(button);
          
          head1.innerText= head1.innerText.slice(0,19)+"   "+deli.length;
          head2.innerText= head2.innerText.slice(0,19)+"   "+feli.length;
          button.addEventListener("click", function(event) {
            var btn = event.target;
            var fff=btn.id;
            // console.log(feli,li,li2,all_li,feli);
            if (fff.slice(0,6)=="temp__")
              {
                // console.log(fff.slice(6));
                fff=parseInt(fff.slice(6));
                btn.setAttribute("class", "btn btn-danger m-3 p-6 btn-lg mybtn");
                btn.setAttribute("type", "button");
                btn.setAttribute("id",fff);
                absent.appendChild(btn);
                
                deli=remove_ele(deli,fff);
                feli.push(fff);
                feli.sort(function(a, b){return a-b});
              }
            else{
                btn.setAttribute("id","temp__"+fff);
                btn.setAttribute("class", "btn btn-success m-3 p-6 btn-lg mybtn");
                btn.setAttribute("type", "button");
                present.appendChild(btn);
                fff=parseInt(fff)
                feli=remove_ele(feli,fff);
                deli.push(parseInt(fff));
                deli.sort(function(a, b){return a-b});
            }
            head1.innerText= head1.innerText.slice(0,19)+"   "+deli.length;
            head2.innerText= head2.innerText.slice(0,19)+"   "+feli.length;
           fun3();
            });
        }
      fun3();
      // console.log("gjkljhgjkl");
     };
fun2();
  fun3();


    
