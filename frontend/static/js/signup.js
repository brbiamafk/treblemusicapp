function signup()
{
    username=document.getElementById("username").value;
    password=document.getElementById("password").value;
    console.log(username, password);

    if(document.getElementById("username").value == "brbiamafk"
       && document.getElementById("password").value == "Peepeepoopoo69!")
    {
        alert("Login successful.");
        location.href="myprofile.html";
    }
    else
    {
        alert( "Incorrect login credentials." );
    }
}
