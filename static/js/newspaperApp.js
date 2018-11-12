var buffer

var app = angular.module('myApp', []);
app.controller('customersCtrl', function($scope, $http) {

    $scope.items = RESULTS;
    $scope.sortType     = 'price'; // set the default sort type
    $scope.sortReverse = false;
    $scope.searchFish = '';     // set the default search/filter term
    $scope.quick_search_key = 'kia';
    $scope.collection_size = 0;
    $scope.today = new Date();
    $scope.isSpecial = false;

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
            url = 'https://kambo.pythonanywhere.com/mongo_quick_search/' + $scope.quick_search_key;
            console.log('quick_search: ', url )

            // $http.get(url).then(function (response)  {
            //     $scope.items = response.data;
            //     // console.log($scope.items)
            //     console.log('response', response)
            //     $scope.showLoader = false;
            //     buffer = $scope.items
            //     $scope.collection_size = response.data[0].price;
            //     $scope.showLoader = false;
            // });
        }

    }

    $scope.init = function (){
        url = 'https://kambo.pythonanywhere.com/mongo_quick_search/' + 'mercedes'
        $scope.showLoader = true;

        // $http.get(url).then(function (response)  {
        //     $scope.items = response.data;

        //     // console.log('http_get: ', $scope.items.title)

        //     $scope.showLoader = false;
        //     buffer = $scope.items
        // });

    }
    angular.element(document).ready($scope.init);

}).filter('telephone', function(){
    return function(input) {
        try{
          return input.split(' ').join('');
        }
        catch(ex){
          return '';
        }

    };
  });

