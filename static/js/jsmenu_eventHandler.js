window.addEventListener('load', function() {

  var homeViewBtn = document.getElementById('btn-home-view');
  var display = document.getElementById('display');

  const mainMenu = ()=> {

      var ul = document.querySelector('ul');

      (showMenu = ()=> {

         tmp ="";

         data.forEach( (x, i) => {
              console.log(x.name, i);

              if ( i == 0){
                tmp += `<li class="active" id="pk${i}">`
              }
              else {
                tmp += `<li id="pk${i}">`
              }
              tmp += `<a data-toggle="tab" href="#menu${i}"> ${x.name}</a> </li>`
         });

       ul.innerHTML = tmp;

    })();




    (tabContent = () => {

      var divtab = document.querySelector('.divtab');
        var str = `<div class="tab-content">`;

        data.forEach( (x, i) => {
            str += `
                  <div id="menu${i}" class="tab-pane fade">
                      <div style="background-color: #f0f0f0;;">` + prodsDom(i) +  `</div>
                  </div> `
         });

        str +=`</div>`


       divtab.innerHTML = str;
    })();


};

    mainMenu();
    document.querySelector('#pk1 a').click();
    console.log('START  >');
});

prodsDom = (index) => {
    str = ``;
    if (data[index].menu == undefined) {
        return "There is no products"
    }
    else {
        data[index].menu.forEach( (m, i) => {

            spanUrl =``

            str +=`<p id="${m.name}" > <h5>${m.name}</h5> </p>`
            if (m.products != undefined) {
                m.products.forEach((p, n) =>{
                    p.url == undefined? spanUrl =`@` : spanUrl = `<span class="purl"> <a href="${p.url}">go</a></span>`
                    str +=`<div style="border-bottom: solid; background: antiquewhite;"> <span class="pname"> ${p.name} </span>
                    <span class="pprice"> $ ${p.price}</span> ${spanUrl}
                    </div> `
                });
            };
        });
    }
    return str;
}


submenu = (index) => {
        return "";
        str = "";
        if(data[index].menu == undefined){
            return "";
        }

        // str = `<ul class="nav nav-tabs submenu">`;
        str = `<ul class="nav submenu">`;
        data[index].menu.forEach( (p, i) => {
            console.log(p);
            str += `<li> <a href="#${p.name}"> ${p.name}</a> </li> `;
        });
        return str + "</ul>";
    }
