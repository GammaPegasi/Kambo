window.addEventListener('load', function() {

  var homeViewBtn = document.getElementById('btn-home-view');
  var display = document.getElementById('display');


  const foo = ()=> {
      var ul = document.querySelector('ul');

      (showMenu = ()=> {

         tmp ="";

         data.forEach( (x, i) => {
              console.log(x.name, i);

              if ( i == 0){
                tmp += `<li class="active">`
              }
              else {
                tmp += `<li>`
              }
              tmp += `<a data-toggle="tab" href="#menu${i}"> ${x.name}</a> </li>`
         });

       ul.innerHTML = tmp;

    })();



    (tabContent = () => {

      var divtab = document.querySelector('.divtab');
        var str = `<div class="tab-content"  style="border: dotted 2px red; height: 150px;">`;

        data.forEach( (x, i) => {
            str += `
                  <div id="menu${i}" class="tab-pane fade">
                      <h4>${x.name}</h4>
                      <div style="background-color: #f0f0f0;;">` + prodsDom(i) +  `</div>
                  </div> `
         });

        str +=`</div>`


       divtab.innerHTML = str;
    })();



};

    foo();

    document.querySelector('ul li a').click();

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

            str +=`<h5>${m.name}</h5>`
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



prods = (index) => {
    if (data[index].menu != undefined) {
        data[index].menu.forEach( (m, i) => {
            console.log(m.name)
            if (m.products != undefined) {
                m.products.forEach((p, n) =>{
                    console.log(p.name, " $", p.price, p.url);
                });
            };
        });
    }
}




