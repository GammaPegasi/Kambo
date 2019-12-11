mongoLabUrl = 'https://api.mlab.com/api/1/databases/timestamps/collections/ML?apiKey=SJENoV9fQLG5t1ZjHA1XUTkyU3KMvadl'


arr =  ['(094) 263705' ,  '099158200' , '091362309' , '098257375' , '(099) 946384' , '(091) 406070' , '(099) 410490']


function cleanString(number) {
	newNum = number.replace('(', '').replace(')', '').replace(/ /g, '').replace(/-/g, '');
	// console.log(newNum)
	return newNum;
}

function isLocalCellPhoneNumber(number){
	return number.length == 9 && number[0] =='0'
}

function eval(number){
	return true
}

function whatsAppLink(number, message){
    return `<a target="_blank" href='https://api.whatsapp.com/send?phone=598${cleanString(number).substr(1)}&text=${message}'> ${cleanString(number)} </a>`
}


function turnIntoWhatsAppNumber(obj){
	buff = '';
	obj.phones.forEach(function(e) {

		newNum = cleanString(e)
		if(isLocalCellPhoneNumber(newNum)){

		    newNum = '098755427'
		    message = 'Hola, podria darme el numero de padron del el terreno publicado en Mercado Libre - Saludos y gracias ' + obj.url
			buff += whatsAppLink(newNum, message)
		}
		else buff += `<p>${newNum}</p>`

	});
	return buff;

}


// slider
// var slideIndex = 1;
// showSlides(slideIndex);

// // Next/previous controls
// function plusSlides(n) {
//   showSlides(slideIndex += n);
// }

// // Thumbnail image controls
// function currentSlide(n) {
//   showSlides(slideIndex = n);
// }

// function showSlides(n) {
//   var i;
//   var slides = document.getElementsByClassName("mySlides");
//   var dots = document.getElementsByClassName("demo");
//   var captionText = document.getElementById("caption");
//   if (n > slides.length) {slideIndex = 1}
//   if (n < 1) {slideIndex = slides.length}
//   for (i = 0; i < slides.length; i++) {
//     slides[i].style.display = "none";
//   }
//   for (i = 0; i < dots.length; i++) {
//     dots[i].className = dots[i].className.replace(" active", "");
//   }
//   slides[slideIndex-1].style.display = "block";
//   dots[slideIndex-1].className += " active";
//   captionText.innerHTML = dots[slideIndex-1].alt;
// }



// function getSliderHTML(e){

//     buffer = ""
//     e.images.forEach((url, index)=> {
//         buffer +=  `
//             <div class="mySlides fade">
//                 <div class="numbertext"> ${index + 1}/ ${e.images.length}</div>
//                 <img src="${url}" style="width:100%">
//                 <div class="text">Caption Text</div>
//             </div>
//             `
//     });

//     return buffer;
// }





