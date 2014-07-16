function AsanasCtrl($scope, $http, $sce) {
    $scope.asanas = [];
    $http.get('/admin/asana').success(function(response) {
        $scope.asanas = response;
    });

    $scope.createAsana = function() {
        var data = {'name': $scope.name,
                    'description': $scope.description,
                    'image_url': $scope.imageUrl};
        $http.post("/admin/asana", data).success(function(data) {
            $scope.asanas.push(data);
            $scope.name = '';
            $scope.description = '';
            $scope.imageUrl = '';
        });
    };
    $scope.trustHTML = function(html) {
        return $sce.trustAsHtml(html);
    };
};
