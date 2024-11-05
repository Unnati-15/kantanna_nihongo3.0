var app = angular.module("NIHONGO", ["ngRoute"])
app.config(function($routeProvider) {
    $routeProvider
        .when("/", {
            templateURL: "ichi.html",
        })
        .when("/BASICS", {
            templateURL: "BASICS.html",
        })
        .when("/HIRAGANA", {
            templateURL: "HIRAGANA.html",
        })
        .when("/KATAKANA", {
            templateURL: "KATAKANA.html",
        })
        .when("KANJI", {
            templateURL: "KANJI.html",
        })
        .when("RESOURCES", {
            templateURL: "RESOURCES.html",
        })
        .when("EXAMS", {
            templateURL: "EXAMS.html",
        })
        .when("CONTACT", {
            templateURL: "CONTACT.html",
        })
        .when("LOGIN/REGISTER", {
            templateURL: "LOGIN/REGISTER.html",
        })
        .otherwise({
            templateUrl: "ichi.html"
        });
});