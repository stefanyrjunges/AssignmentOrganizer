<h1>Assignment Organizer with Due Notifications</h1>
<p align="justify">
A Python project written for personal use, aiming to streamline the assignment management process, providing a centralized platform for tracking and
staying updated on upcoming deadlines. By combining intuitive user interface design with automated notifications, the application aims to enhance productivity and reduce
the likelihood of missed deadlines.
</p>

<h3>Description</h3>
<p align="justify">
The Assignment Organizer with Due Date Notifications is a Python application developed using Tkinter for the graphical user interface (GUI) and openpyxl for Excel sheet manipulation.
It serves as a tool for users to manage their assignments efficiently.

The user interface prompts the user to input assignment details such as name, module, and due date, along with a status flag indicating whether the assignment is completed or not.
Upon submission, the data is saved to an Excel file specified by the filepath. If the file doesn't exist, it creates a new Excel workbook with the specified headers and saves the data.
If the file exists, it appends the data to the existing workbook. 

The application also includes a feature for due date notifications, checking the Excel sheet for upcoming due dates. When the current date matches a due date, the application sends a notification to the user's
phone, reminding them of the impending deadline.
</p>

<h3>What can be found in the codes</h3>
<p align="justify">
🖱️AssignmentOrganizer.py
  <br>
<li>Tkinter library to develop the Graphical User Interface, including frames to organize the layout, labels, entries, combobox and buttons;</li>
<li>Openpyxl module to create, modify and extract data from Excel spreadsheet;</li>
<li>os module to check if the excel file exists before saving the data;</li>
<li>Datetime module to manipulate dates;</li>
<li>strptime() method to convert the date to a DD/MM/YYYY format; </li>
<li>'Try' and 'Except' statements to handle errors when attempting to convert the dates;</li>
<li>Functions for specific tasks such as entering data, cancelling the operation and handling window closing events;</li>
<li>Different message boxes to provide guidance and assistance to the user.</li>
<br>
🖱️Notification.py
  <br><br>
<li>Openpyxl module to create, modify and extract data from Excel spreadsheet;</li>
<li>Datetime module to manipulate dates; </li>
<li>Requests module to send notifications to the user’s phone;</li>
<li>strptime() and strftime() methods to convert dates to a DD/MM/YYYY format;</li>
<li>strptime() method to convert the date to a DD/MM/YYYY format; </li>
<li>'For' loop that iterates over pairs of values to check dates in the excel sheet;</li>
<li>'Try' and 'Except' statements to handle errors when attempting to convert the dates;</li>
<li>isinstance() method to check if the date is in the correct format.</li>
</p>

<h3>Preview</h3>
<img src="https://raw.githubusercontent.com/stefanyrjunges/AssignmentOrganizer/main/AssignmentOrganizer_PREVIEW.png">

<h3>Inspiration</h3>
<p align="justify">
<a href="https://www.youtube.com/watch?v=fvIThtPt6Nc&ab_channel=CodeFirstwithHala">Code First with Hala</a>
</p>
