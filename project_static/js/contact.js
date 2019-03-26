$(document).ready(function(){
    
    (function($) {
        "use strict";

    
    jQuery.validator.addMethod('answercheck', function (value, element) {
        return this.optional(element) || /^\bcat\b$/.test(value)
    }, "type the correct answer -_-");

    $(function() {
        var valid = $('#contactForm').data('valid')
        if (valid != ""){
            if (valid == "True") {
                $('#contactForm').fadeTo( "slow", 1, function() {
                    $(this).find('label').css('cursor','default');
                    $('#success').fadeIn()
                    $('.modal').modal('hide');
                    $('#success').modal('show');
                })
            }
            else {
                $('#contactForm').fadeTo( "slow", 1, function() {
                    $('#error').fadeIn()
                    $('.modal').modal('hide');
                    $('#error').modal('show');
                })
            }
        }
    })
        
 })(jQuery)
})

