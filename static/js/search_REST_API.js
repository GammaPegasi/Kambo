console.log("START")

var app = angular.module('search_REST_API', []);

app.controller('MainCtrl', function($scope,$http ) {
    $scope.name = 'The world is mine';
    $scope.price = 32145;
    $scope.data = "{id: '1___1', name: '___Florida___'},";
    $scope.searchKey = "t"

  $scope.submit = function () {
    console.log("SUBMIT: ");
    $http.get("https://kambo.pythonanywhere.com/car_view/?format=json&search=" + $scope.searchKey)
        .then(function(response) {
            // $scope.data = response.data;
            $scope.data = response;
            // console.log("*********")
            // console.log($scope.data)
        });
  };

  $scope.submit()

});


