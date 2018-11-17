function validate_repeated_digits(inputStr){
	const digits_ocurrences = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
	for ( i = 0; i < inputStr.length; i++){
			j = Number(inputStr[i])
			if (j != 0) {
     			digits_ocurrences[j]  += 1;
    			if (digits_ocurrences[j] > TRESHOLD)
     				return false
			}
	}
	return true
}

function highlightWrongValues(){
        q = document.querySelectorAll('.highligAble')
        q.forEach( function (e,i){
                if(e.innerText == '?'){
                  e.style.fontSize = '2em';
                  e.style.color = 'blue';
                }
        });
}

var app = angular.module('myApp', []);
app.controller('customersCtrl', function($scope, $http) {

    var buffer
    $scope.items = [];
    $scope.sortType     = 'price'; // set the default sort type
    $scope.sortReverse = false;
    $scope.searchFish = '';     // set the default search/filter term
    $scope.quick_search_key = '';
    $scope.collection_size = 0;
    $scope.today = new Date();
    $scope.isSpecial = false;

    $scope.updateCSS = function(){

        return highlightWrongValues()
    }

    $scope.set_order_key = function (key){

        $scope.isSpecial = ! $scope.isSpecial;
        if (key == 'seller_address.state.name')
            key = 'location';
        if ($scope.sortType == key)
            $scope.sortReverse = ! $scope.sortReverse
        else {
            old_key = $scope.sortType
            $scope.sortType = key;
            $('#' + old_key).css({ "font-size" : "" });
            $('#' + key).css({ "font-size" : "initial" });
        };
        console.log(key);
    }

    $scope.sortReverse  = false;  // set the default sort order

    $scope.quick_search = function(){
        $scope.showLoader = true;

        if ($scope.quick_search_key != ''){
            url = '/mongo_quick_search/' + $scope.quick_search_key;

	    console.log('quick_search: ', url )

            $http.get(url).then(function (response)  {
                $scope.items = response.data;
                console.log($scope.items, '.....>>>')
                console.log('response', response)
                $scope.showLoader = false;
                buffer = $scope.items
                $scope.collection_size = response.data[0].price;
                $scope.showLoader = false;
            });
        }
        setTimeout(function(){ $scope.init_popups(); console.log("init_PP"); }, 3000);
    }

    $scope.init_popups = function (){
        console.log("POP UPS ON: [" , $scope.items.length , "]");
        highlightWrongValues()
        $('[data-toggle="popover"]').popover({
          html: true,
          trigger: 'hover',
          placement: 'bottom',
           content: function(){return '<img src="'+$(this).data('img') + '" width=250px height=250px />';}
        });
    };

    $scope.init = function (){
        url = '/mongo_quick_search/' + 'a'

        $scope.showLoader = true;
        $http.get(url).then(function (response)  {
            $scope.items = response.data;
            $scope.showLoader = false;
            buffer = $scope.items;
            setTimeout(function(){ $scope.init_popups(); console.log("init_PP"); }, 3000);
        });
    };

    angular.element(document).ready($scope.init);

    $scope.valid_mileage = function(){

        STYLE_WRONG = 'id="wrg"'
        return STYLE_WRONG

        f(input == 0)
            return 0;
        INVALID_DATA = "?"
        TRESHOLD = 3
    	inputStr = input.toString()
    	if(inputStr.length < 4) return STYLE_WRONG
    	if(inputStr.includes('123')) return STYLE_WRONG

        else return ""
    };

}).filter('telephone', function(){
        return function(input) {
                try{
                  return input.split(' ').join('');
                }
                catch(ex){
                  return '';
                }
            };

	    inputStr = input.toString()
    	    if(inputStr.length < 4) return INVALID_DATA

}).filter('validatePrice', function(){
    return function(input, currency_id , index) {

        INVALID_DATA = "?"
        TRESHOLD = 3
    	inputStr = input.toString()
    	if(inputStr.length < 4 || inputStr.includes('123')) {
    	    return INVALID_DATA
    	}

        if(validate_repeated_digits(inputStr))
            return currency_id + ' ' + input.toLocaleString('de-DE', {maximumSignificanDigits: 8})
        else{
            // document.querySelector(selector).classList.add("wrongPrice")
            return INVALID_DATA
        };
    };

}).filter('validateMileage', function(){
    return function(input, index) {
        if(input == 0)
            return 0;
        INVALID_DATA = "?"
        TRESHOLD = 3
    	inputStr = input.toString()
    	if(inputStr.length < 4 || inputStr.includes('123')) {
    	    return INVALID_DATA
    	}

        if(validate_repeated_digits(inputStr))
            return input.toLocaleString('de-DE', {maximumSignificanDigits: 8}) + ' ' +  'KM'
        else return INVALID_DATA
    };
});
