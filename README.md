
Steps to run project 
1. Clone the repository

2.create a virtual environment

3.py -m venv venv

4. Activate the virtual environment by cd ./venv/Scripts/activate

5. install all the dependencies by pip install -r requirements
6. show  migration of model using  python manage.py makemigrations
7. migrate the model using python manage.py migrate

8. now create a user using api/users/create

   Username  ,mail ,pasword ,first_name ,last_name are required

9. after creating the user create a task using api/tasks/create
    ->task_name ,description ,


10. Assign the task using api/tasks/<int:pk>/assign 
     -> taking the user_ids as post body
     ->then assign the task to that users_ids

11. Get the users assign task by using the users/<user_id/tasks/

