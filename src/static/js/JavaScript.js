$(function() {
	$(".btn").click(function() {
		$(".form-signin").toggleClass("form-signin-left");
    $(".form-signup").toggleClass("form-signup-left");
    $(".frame").toggleClass("frame-long");
    $(".signup-inactive").toggleClass("signup-active");
    $(".signin-active").toggleClass("signin-inactive");
    $(".forgot").toggleClass("forgot-left");   
    $(this).removeClass("idle").addClass("active");
	});
});

$(function() {
	$(".btn-signup").click(function() {
  $(".nav").toggleClass("nav-up");
  $(".form-signup-left").toggleClass("form-signup-down");
  $(".success").toggleClass("success-left"); 
  $(".frame").toggleClass("frame-short");
	});
});

$(function() {
	$(".btn-signin").click(function() {
  $(".btn-animate").toggleClass("btn-animate-grow");
  $(".welcome").toggleClass("welcome-left");
  $(".cover-photo").toggleClass("cover-photo-down");
  $(".frame").toggleClass("frame-short");
  $(".profile-photo").toggleClass("profile-photo-down");
  $(".btn-goback").toggleClass("btn-goback-up");
  $(".forgot").toggleClass("forgot-fade");
	});
});

function obtenerDatos(id){
  document.getElementById('formulario').action ='/editar_persona/'+id
  document.getElementById('boton_form').innerHTML='Actualizar'

  nombreactual   = document.getElementById('tabla_nombre'+id).innerHTML
  apellidoactual = document.getElementById('tabla_apellido'+id).innerHTML
  telefonoactual = document.getElementById('tabla_telefono'+id).innerHTML//innerHtml: extraer el formulario que esta en index

  document.getElementById('nombre').value   = nombreactual
  document.getElementById('apellido').value = apellidoactual
  document.getElementById('telefono').value = telefonoactual
}