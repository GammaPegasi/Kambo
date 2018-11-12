
// var grid = document.querySelector('.intro-grid');
var grid = document.querySelector('.test-grid');

function addElement(i) {
 	var mydiv = document.createElement("div");
	mydiv.className = 'item'
	mydiv.style.backgroundColor = '#f9f7f1'
	mydiv.style.border = 'doted'
	mydiv.style.borderWidth = '1px'

	var title = document.createElement("div");
	title.className = 'mytitle'
	var t = document.createTextNode(RESULTS[i].title);
    title.appendChild(t);


	var price = document.createElement("div");
	price.className = 'myprice'
	var t = document.createTextNode( RESULTS[i].currency_id + " " + RESULTS[i].price);
    price.appendChild(t);

	var description = document.createElement("p");
    var d = document.createTextNode(RESULTS[i].description);
    description.appendChild(d);
    description.className = 'description'

	var phone = document.createElement("span");
    var d = document.createTextNode(RESULTS[i].seller_contact.area_code + RESULTS[i].seller_contact.phone);
    phone.appendChild(d);
    phone.className = 'phone'

	var location = document.createElement("span");
    var d = document.createTextNode(RESULTS[i].seller_address.state.name + " " + RESULTS[i].seller_address.city.name);
    location.appendChild(d);
    location.className = 'location'

    var image = document.createElement("img");
    image.src = '/static/img/' + RESULTS[i].main_img;
    image.className = 'myimage'

    mydiv.appendChild(title);
    mydiv.appendChild(price);
	mydiv.appendChild(image);
	mydiv.appendChild(description);
	mydiv.appendChild(phone);
	mydiv.appendChild(location);

	// mydiv.firstElementChild.width = 200
	// mydiv.firstElementChild.height = 200
    return mydiv;
}

for (i = 0; i < 12; i++){
	elem = addElement(i);
	console.log(i, elem, grid)

	salvattore.appendElements(grid, [elem]);
}
