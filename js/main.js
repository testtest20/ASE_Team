let addNewList = document.querySelector(".addNew");
let overlay = document.querySelector(".overlay");
let addNewDiv = document.querySelector(".addNewContact");
let close = document.querySelector(".close");

function openlay() {
    addNewDiv.style.display = "block";
    overlay.style.display = "block";
}
function closelay() {
    addNewDiv.style.display = "none";
    overlay.style.display = "none";
}

addNewList.addEventListener('click', openlay);
close.addEventListener('click', closelay);
// search
addNewPer = document.querySelector(".adduser");
let over = document.querySelector(".over");
let addNewuser = document.querySelector(".user");
let shut = document.querySelector(".shut");


function openform() {
    addNewuser.style.display = "block";
    over.style.display = "block";
}
function closeform() {
    addNewuser.style.display = "none";
    over.style.display = "none";
}

addNewPer.addEventListener('click', openform);
shut.addEventListener('click', closeform);

// user

let addWishList = document.querySelector(".addwish");
let wishList = document.querySelector(".wish_list");
let closew = document.querySelector(".closew")
let pro = document.querySelector(".products");

function openwish() {
    wishList.style.display = "block";
    pro.style.display = "none";
}
function closewish() {
    wishList.style.display = "none";
    pro.style.display = "block";
}

addWishList.addEventListener('click', openwish);
closew.addEventListener('click', closewish);

//wish_list


{% for product in orderpage %}

$(".cat{{product.category.id}}").click(function(){
   $(".producthide").hide()
   $(".product{{product.category.id}}").show()
});


{% endfor %}
