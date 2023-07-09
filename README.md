<h1 align = "center">Project: AirBnB clone</h1>
<img src="https://github.com/Mishel450/holbertonschool-AirBnB_clone/assets/124268926/826d025a-9b16-4a60-b75d-f7dd08f183a2">

<p>The HBHN project is part of the second quarter of the Software program at Holberton School. Its main goal is to develop a complete clone of the well-known web application AirBnB, covering all technological layers (back-end).</p>

<img src="https://github.com/Mishel450/holbertonschool-AirBnB_clone/assets/124268926/5942cb22-f6e2-4785-a58a-be8fd501e8a8">

<h2>Requirements</h2>

<li>All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)</li>
<li>Your code should use the pycodestyle (version 2.7.*)</li>
<li>That the README.md file exists.</li>
<li>You have to use the unittest module</li>

<h2>Console archive files</h2>

 <h3><a href="https://github.com/Mishel450/holbertonschool-AirBnB_clone/blob/master/models/base_model.py">BaseModel</a></h3>
<p>
    Defines all common attributes/methods that will be inherited by other future classes. 
    <li><b>def __init__(self, *args, **kwargs):</b> Initialize an instance of the class when a new object is created.</li>
    <li><b>def __str__(self):</b>String representation of the BaseModel class</li>
    <li><b>def save(self):</b>Updates the public instance attribute updated_at with the current datetime</li>
    <li><b>def to_dict(self):</b>Returns a dictionary containing all keys/values of __dict__ of the instance</li>
</p>
<table>
    <tr>
        <td><b>Name of class</b></td>
        <td><b>Attributes</b></td>
    </tr>
    <tr>
        <td>BaseModel</td>
        <td><li>id</li>
            <li>create_at</li>
            <li>update_at</li></td>
    </tr>
    <tr>
        <td>User</td>
        <td><li>email</li>
            <li>password</li>
            <li>first_name</li>
            <li>last_name</li></td>
    </tr>
    <tr>
        <td>City</td>
        <td><li>state_id</li>
            <li>name</li></td>
    </tr>
    <tr>
        <td>Amenity</td>
        <td><li>name</li></td>
    </tr>
    <tr>
        <td>State</td>
        <td><li>name</li></td>
    </tr>
    <tr>
        <td>Place</td>
        <td><li>city_id</li>
            <li>user_id</li>
            <li>name</li>
            <li>description</li>
            <li>number_room</li>
            <li>number_bathrooms</li>
            <li>max_guest</li>
            <li>price_by_night</li>
            <li>latitude</li>
            <li>longitude</li>
            <li>amenity_ids</li>
            <li>Amenity.if</li></td>
    </tr>
    <tr>
        <td>Review</td>
        <td><li>place_id</li>
            <li>user_id</li>
            <li>text</li></td>
    </tr>
</table>

 <h3><a href="https://github.com/Mishel450/holbertonschool-AirBnB_clone/blob/master/console.py">Console</a></h3>
<p>
    Contains the entry point of the command interpreter
</p>
<table>
    <tr>
        <td><b>Function</b></td>
        <td><b>Description</b></td>
        <td><b>Example</b></td>
    </tr>
    <tr>
        <td>do_quit</td>
        <td>This do_quit function would be used to terminate or exit the program you are in.</td>
        <td>quit</td>
    </tr>
    <tr>
        <td>do_EOF</td>
        <td>Handle the end of the program when the end of the input file is reached</td>
        <td>ctrl + D</td>
    </tr>
    <tr>
        <td>emptyline</td>
        <td>Do nothing</td>
        <td>empty line + enter</td>
    </tr>
    <tr>
        <td>do_create</td>
        <td>Creates a new instance of a class</td>
        <td>create User</td>
    </tr>
    <tr>
        <td>do_show</td>
        <td>This function prints the string representation of an instance based on the class name and instance ID.</td>
        <td>show Place</td>
    </tr>
    <tr>
        <td>do_destroy</td>
        <td>Delete an instance based on the class name and its identifier (id).</td>
        <td>destroy User</td>
    </tr>
    <tr>
        <td>do_all</td>
        <td> this function prints the string representation of all instances stored in the "objects" object.</td>
        <td>all or all Review</td>
    </tr>
    <tr>
        <td>do_update</td>
        <td>This function is responsible for updating an instance based on the provided class name and identifier (id), adding or updating an attribute.</td>
        <td>update User a1s54321-c2b6-43vc-9825-2b9edff464f1 email "AirBnB@gmail.com"</td>
    </tr>
</table>


 <h3><a href="https://github.com/Mishel450/holbertonschool-AirBnB_clone/blob/master/models/engine/file_storage.py">File_storage</a></h3>
<p>
    Serializes instances to a JSON file and deserializes JSON file to instances
</p>
<table>
    <tr>
        <td><b>Function</b></td>
        <td><b>Description</b></td>
    </tr>
    <tr>
        <td>all</td>
        <td>This function returns the __objects dictionary containing the stored objects.</td>
    </tr>
    <tr>
        <td>new</td>
        <td>creates a new instance</td>
    </tr>
    <tr>
        <td>save</td>
        <td>serializes the objects stored in the __objects dictionary to a JSON file</td>
    </tr>
    <tr>
        <td>reload</td>
        <td>deserializes a JSON file and recreates the corresponding objects</td>
    </tr>
</table>
<details>
 <summary><h3>Authors</h3></summary>
    
<h5><a href="https://github.com/Mishel450">Mishel Tomas</a></h5>
<h5><a href="https://github.com/DarianGrabino">Darian Grabino</a></h5>
<h5><a href="https://github.com/20Emi">Emily Sánchez</a></h5>
</derails>
