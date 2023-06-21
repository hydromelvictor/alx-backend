
Curriculum
Short Specializations
Average: 103.68%
You just released the advanced tasks of this project. Have fun!
0x03. Queuing System in JS
Back-end
JavaScript
ES6
Redis
NodeJS
ExpressJS
Kue
 By: Johann Kerbrat, Engineering Manager at Uber Works
 Weight: 1
 Project will start Jun 19, 2023 3:00 AM, must end by Jun 22, 2023 3:00 AM
 Manual QA review must be done (request it when you are done with the project)


Resources
Read or watch:

Redis quick start
Redis client interface
Redis client for Node JS
Kue deprecated but still use in the industry
Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

How to run a Redis server on your machine
How to run simple operations with the Redis client
How to use a Redis client with Node JS for basic operations
How to store hash values in Redis
How to deal with async operations with Redis
How to use Kue as a queue system
How to build a basic Express app interacting with a Redis server
How to the build a basic Express app interacting with a Redis server and queue
Requirements
All of your code will be compiled/interpreted on Ubuntu 18.04, Node 12.x, and Redis 5.0.7
All of your files should end with a new line
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the js extension
Required Files for the Project
package.json
Click to show/hide file contents
.babelrc
Click to show/hide file contents
and…
Don’t forget to run $ npm install when you have the package.json

Tasks
0. Install a redis instance
mandatory
Download, extract, and compile the latest stable Redis version (higher than 5.0.7 - https://redis.io/download/):

Téléchargez, extrayez et compilez la dernière version stable de Redis (supérieure à 5.0.7 - https://redis.io/download/) :

$ wget http://download.redis.io/releases/redis-6.0.10.tar.gz
$ tar xzf redis-6.0.10.tar.gz
$ cd redis-6.0.10
$ make
Start Redis in the background with src/redis-server
Démarrer Redis en arrière-plan avec src/redis-server
$ src/redis-server &
Make sure that the server is working with a ping src/redis-cli ping
Vérifiez que le serveur fonctionne avec un ping src/redis-cli ping
PONG
Using the Redis client again, set the value School for the key Holberton
En utilisant à nouveau le client Redis, définissez la valeur School pour la clé Holberton
127.0.0.1:[Port]> set Holberton School
OK
127.0.0.1:[Port]> get Holberton
"School"
Kill the server with the process id of the redis-server (hint: use ps and grep)
Tuer le serveur avec l'identifiant de processus du serveur redis (hint : utiliser ps et grep)
$ kill [PID_OF_Redis_Server]
Copy the dump.rdb from the redis-5.0.7 directory into the root of the Queuing project.

Requirements:

Running get Holberton in the client, should return School

Copiez le fichier dump.rdb du répertoire redis-5.0.7 à la racine du projet Queuing.

Exigences :

Lancer get Holberton dans le client, devrait retourner School

Repo:

GitHub repository: alx-backend
Directory: 0x03-queuing_system_in_js
File: README.md, dump.rdb
  
1. Node Redis Client
mandatory
Install node_redis using npm

Using Babel and ES6, write a script named 0-redis_client.js. It should connect to the Redis server running on your machine:

It should log to the console the message Redis client connected to the server when the connection to Redis works correctly
It should log to the console the message Redis client not connected to the server: ERROR_MESSAGE when the connection to Redis does not work
Requirements:

To import the library, you need to use the keyword import

Installer node_redis avec npm

En utilisant Babel et ES6, écrivez un script nommé 0-redis_client.js. Il doit se connecter au serveur Redis qui tourne sur votre machine :

Il doit afficher dans la console le message Redis client connected to the server (client Redis connecté au serveur) lorsque la connexion à Redis fonctionne correctement.
Il doit afficher dans la console le message Redis client not connected to the server : ERROR_MESSAGE lorsque la connexion à Redis ne fonctionne pas.
Exigences :

Pour importer la bibliothèque, vous devez utiliser le mot-clé import

bob@dylan:~$ ps ax | grep redis-server
 2070 pts/1    S+     0:00 grep --color=auto redis-server
bob@dylan:~$ 
bob@dylan:~$ npm run dev 0-redis_client.js 

> queuing_system_in_js@1.0.0 dev /root
> nodemon --exec babel-node --presets @babel/preset-env "0-redis_client.js"

[nodemon] 2.0.4
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `babel-node --presets @babel/preset-env 0-redis_client.js`
Redis client not connected to the server: Error: Redis connection to 127.0.0.1:6379 failed - connect ECONNREFUSED 127.0.0.1:6379
Redis client not connected to the server: Error: Redis connection to 127.0.0.1:6379 failed - connect ECONNREFUSED 127.0.0.1:6379
Redis client not connected to the server: Error: Redis connection to 127.0.0.1:6379 failed - connect ECONNREFUSED 127.0.0.1:6379
^C
bob@dylan:~$ 
bob@dylan:~$ ./src/redis-server > /dev/null 2>&1 &
[1] 2073
bob@dylan:~$ ps ax | grep redis-server
 2073 pts/0    Sl     0:00 ./src/redis-server *:6379
 2078 pts/1    S+     0:00 grep --color=auto redis-server
bob@dylan:~$
bob@dylan:~$ npm run dev 0-redis_client.js 

> queuing_system_in_js@1.0.0 dev /root
> nodemon --exec babel-node --presets @babel/preset-env "0-redis_client.js"

[nodemon] 2.0.4
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `babel-node --presets @babel/preset-env 0-redis_client.js`
Redis client connected to the server
^C
bob@dylan:~$
Repo:

GitHub repository: alx-backend
Directory: 0x03-queuing_system_in_js
File: 0-redis_client.js
  
2. Node Redis client and basic operations
mandatory
In a file 1-redis_op.js, copy the code you previously wrote (0-redis_client.js).

Add two functions:

setNewSchool:
It accepts two arguments schoolName, and value.
It should set in Redis the value for the key schoolName
It should display a confirmation message using redis.print
displaySchoolValue:
It accepts one argument schoolName.
It should log to the console the value for the key passed as argument
At the end of the file, call:

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
Requirements:

Use callbacks for any of the operation, we will look at async operations later

Dans un fichier 1-redis_op.js, copiez le code que vous avez écrit précédemment (0-redis_client.js).

Ajoutez deux fonctions :

setNewSchool :
Elle accepte deux arguments schoolName, et value.
Elle doit définir dans Redis la valeur de la clé schoolName.
Elle doit afficher un message de confirmation à l'aide de redis.print
displaySchoolValue :
Elle accepte un argument schoolName.
Il doit enregistrer dans la console la valeur de la clé passée en tant qu'argument.
À la fin du fichier, appelez :

displaySchoolValue('Holberton') ;
setNewSchool('HolbertonSanFrancisco', '100') ;
displaySchoolValue('HolbertonSanFrancisco') ;
Exigences :

Utiliser des callbacks pour toutes les opérations, nous verrons les opérations asynchrones plus tard.

bob@dylan:~$ npm run dev 1-redis_op.js 

> queuing_system_in_js@1.0.0 dev /root
> nodemon --exec babel-node --presets @babel/preset-env "1-redis_op.js"

[nodemon] 2.0.4
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `babel-node --presets @babel/preset-env 1-redis_op.js`
Redis client connected to the server
School
Reply: OK
100
^C

bob@dylan:~$
Repo:

GitHub repository: alx-backend
Directory: 0x03-queuing_system_in_js
File: 1-redis_op.js
  
3. Node Redis client and async operations
mandatory
In a file 2-redis_op_async.js, let’s copy the code from the previous exercise (1-redis_op.js)

Using promisify, modify the function displaySchoolValue to use ES6 async / await

Same result as 1-redis_op.js


Dans un fichier 2-redis_op_async.js, copions le code de l'exercice précédent (1-redis_op.js)

En utilisant promisify, modifions la fonction displaySchoolValue pour utiliser ES6 async / await

Même résultat que 1-redis_op.js


bob@dylan:~$ npm run dev 2-redis_op_async.js

> queuing_system_in_js@1.0.0 dev /root
> nodemon --exec babel-node --presets @babel/preset-env "2-redis_op_async.js"

[nodemon] 2.0.4
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `babel-node --presets @babel/preset-env 2-redis_op_async.js`
Redis client connected to the server
School
Reply: OK
100
^C

bob@dylan:~$
Repo:

GitHub repository: alx-backend
Directory: 0x03-queuing_system_in_js
File: 2-redis_op_async.js
  
4. Node Redis client and advanced operations
mandatory
In a file named 4-redis_advanced_op.js, let’s use the client to store a hash value

Create Hash:
Using hset, let’s store the following:

The key of the hash should be HolbertonSchools
It should have a value for:
Portland=50
Seattle=80
New York=20
Bogota=20
Cali=40
Paris=2
Make sure you use redis.print for each hset
Display Hash:
Using hgetall, display the object stored in Redis. It should return the following:

Requirements:

Use callbacks for any of the operation, we will look at async operations later

Dans un fichier nommé 4-redis_advanced_op.js, utilisons le client pour stocker une valeur de hachage

Créer un hachage :
En utilisant hset, stockons ce qui suit :

La clé du hachage doit être HolbertonSchools
Elle doit contenir une valeur pour :
Portland=50
Seattle=80
New York=20
Bogota=20
Cali=40
Paris=2
Assurez-vous d'utiliser redis.print pour chaque hset
Afficher le hash :
En utilisant hgetall, affichez l'objet stocké dans Redis. Le résultat devrait être le suivant :

Exigences :

Utilisez des callbacks pour toutes les opérations, nous verrons les opérations asynchrones plus tard.


bob@dylan:~$ npm run dev 4-redis_advanced_op.js 

> queuing_system_in_js@1.0.0 dev /root
> nodemon --exec babel-node --presets @babel/preset-env "4-redis_advanced_op.js"

[nodemon] 2.0.4
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `babel-node --presets @babel/preset-env 4-redis_advanced_op.js`
Redis client connected to the server
Reply: 1
Reply: 1
Reply: 1
Reply: 1
Reply: 1
Reply: 1
{
  Portland: '50',
  Seattle: '80',
  'New York': '20',
  Bogota: '20',
  Cali: '40',
  Paris: '2'
}
^C
bob@dylan:~$
Repo:

GitHub repository: alx-backend
Directory: 0x03-queuing_system_in_js
File: 4-redis_advanced_op.js
  
5. Node Redis client publisher and subscriber
mandatory
In a file named 5-subscriber.js, create a redis client:

On connect, it should log the message Redis client connected to the server
On error, it should log the message Redis client not connected to the server: ERROR MESSAGE
It should subscribe to the channel holberton school channel
When it receives message on the channel holberton school channel, it should log the message to the console
When the message is KILL_SERVER, it should unsubscribe and quit
In a file named 5-publisher.js, create a redis client:

On connect, it should log the message Redis client connected to the server
On error, it should log the message Redis client not connected to the server: ERROR MESSAGE
Write a function named publishMessage:
It will take two arguments: message (string), and time (integer - in ms)
After time millisecond:
The function should log to the console About to send MESSAGE
The function should publish to the channel holberton school channel, the message passed in argument after the time passed in arguments
At the end of the file, call:
publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);
Requirements:

You only need one Redis server to execute the program
You will need to have two node processes to run each script at the same time

Dans un fichier nommé 5-subscriber.js, créez un client redis :

En cas de connexion, il doit afficher le message Redis client connected to the server (client Redis connecté au serveur)
En cas d'erreur, il doit afficher le message Redis client not connected to the server : MESSAGE D'ERREUR
Il doit s'abonner au canal de l'école holberton.
Lorsqu'il reçoit un message sur le canal holberton school channel, il doit enregistrer le message dans la console.
Lorsque le message est KILL_SERVER, il doit se désabonner et quitter.
Dans un fichier nommé 5-publisher.js, créez un client redis :

En cas de connexion, il doit afficher le message Redis client connected to the server (client Redis connecté au serveur).
En cas d'erreur, il doit afficher le message Redis client not connected to the server : MESSAGE D'ERREUR
Écrivez une fonction nommée publishMessage :
Elle prendra deux arguments : message (chaîne de caractères) et time (entier - en ms).
Après le temps, une milliseconde :
La fonction doit envoyer un log à la console About to send MESSAGE
La fonction doit publier sur le canal holberton school channel, le message passé en argument après le temps passé en arguments
A la fin du fichier, appeler :
publishMessage("Holberton Student #1 starts course", 100) ;
publishMessage("L'élève n°2 de Holberton commence le cours", 200) ;
publishMessage("KILL_SERVER", 300) ;
publishMessage("L'étudiant n°3 de Holberton commence le cours", 400) ;
Exigences :

Vous n'avez besoin que d'un seul serveur Redis pour exécuter le programme
Vous aurez besoin de deux processus de nœuds pour exécuter chaque script en même temps.

Terminal 1:

bob@dylan:~$ npm run dev 5-subscriber.js 

> queuing_system_in_js@1.0.0 dev /root
> nodemon --exec babel-node --presets @babel/preset-env "5-subscriber.js"

[nodemon] 2.0.4
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `babel-node --presets @babel/preset-env 5-subscriber.js`
Redis client connected to the server
Terminal 2:

bob@dylan:~$ npm run dev 5-publisher.js 

> queuing_system_in_js@1.0.0 dev /root
> nodemon --exec babel-node --presets @babel/preset-env "5-publisher.js"

[nodemon] 2.0.4
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `babel-node --presets @babel/preset-env 5-publisher.js`
Redis client connected to the server
About to send Holberton Student #1 starts course
About to send Holberton Student #2 starts course
About to send KILL_SERVER
About to send Holberton Student #3 starts course
^C
bob@dylan:~$ 
And in the same time in Terminal 1:

Redis client connected to the server
Holberton Student #1 starts course
Holberton Student #2 starts course
KILL_SERVER
[nodemon] clean exit - waiting for changes before restart
^C
bob@dylan:~$ 
Now you have a basic Redis-based queuing system where you have a process to generate job and a second one to process it. These 2 processes can be in 2 different servers, which we also call “background workers”.

Vous disposez à présent d'un système de file d'attente de base basé sur Redis, dans lequel un processus génère un travail et un second le traite. Ces deux processus peuvent se trouver sur deux serveurs différents, que nous appelons également "travailleurs en arrière-plan".

Repo:

GitHub repository: alx-backend
Directory: 0x03-queuing_system_in_js
File: 5-subscriber.js, 5-publisher.js
  
6. Create the Job creator
mandatory
In a file named 6-job_creator.js:

Create a queue with Kue
Create an object containing the Job data with the following format:
{
  phoneNumber: string,
  message: string,
}
Create a queue named push_notification_code, and create a job with the object created before
When the job is created without error, log to the console Notification job created: JOB ID
When the job is completed, log to the console Notification job completed
When the job is failing, log to the console Notification job failed


Dans un fichier nommé 6-job_creator.js :

Créer une file d'attente avec Kue
Créer un objet contenant les données du Job avec le format suivant :
{
  phoneNumber : string,
  message : chaîne,
}
Créez une file d'attente nommée push_notification_code, et créez un job avec l'objet créé précédemment
Lorsque le job est créé sans erreur, enregistrez dans la console Notification job created : JOB ID
Lorsque le travail est terminé, la console affiche un message Notification job completed (travail de notification terminé).
Lorsque le travail échoue, la console Notification job failed (Échec du travail de notification) est affichée.


bob@dylan:~$ npm run dev 6-job_creator.js 

> queuing_system_in_js@1.0.0 dev /root
> nodemon --exec babel-node --presets @babel/preset-env "6-job_creator.js"

[nodemon] 2.0.4
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `babel-node --presets @babel/preset-env 6-job_creator.js`
Notification job created: 1

Nothing else will happen - to process the job, go to the next task!

If you execute multiple time this file, you will see the JOB ID increasing - it means you are storing new job to process…


Rien d'autre ne se produira - pour traiter le travail, passez à la tâche suivante !

Si vous exécutez plusieurs fois ce fichier, vous verrez l'ID JOB augmenter - cela signifie que vous stockez un nouveau job à traiter...

Repo:

GitHub repository: alx-backend
Directory: 0x03-queuing_system_in_js
File: 6-job_creator.js
  
7. Create the Job processor
mandatory
In a file named 6-job_processor.js:

Create a queue with Kue
Create a function named sendNotification:
It will take two arguments phoneNumber and message
It will log to the console Sending notification to PHONE_NUMBER, with message: MESSAGE
Write the queue process that will listen to new jobs on push_notification_code:
Every new job should call the sendNotification function with the phone number and the message contained within the job data
Requirements:

You only need one Redis server to execute the program
You will need to have two node processes to run each script at the same time
You muse use Kue to set up the queue

Dans un fichier nommé 6-job_processor.js :

Créer une file d'attente avec Kue
Créez une fonction nommée sendNotification :
Elle prendra deux arguments phoneNumber et message
Elle affichera dans la console Sending notification to PHONE_NUMBER, with message : MESSAGE
Écrire le processus de file d'attente qui écoutera les nouveaux travaux sur push_notification_code :
Chaque nouveau travail doit appeler la fonction sendNotification avec le numéro de téléphone et le message contenus dans les données du travail.
Exigences :

Vous n'avez besoin que d'un seul serveur Redis pour exécuter le programme
Vous aurez besoin de deux processus de nœuds pour exécuter chaque script en même temps.
Vous pouvez utiliser Kue pour mettre en place la file d'attente.

Terminal 2:

bob@dylan:~$ npm run dev 6-job_processor.js 

> queuing_system_in_js@1.0.0 dev /root
> nodemon --exec babel-node --presets @babel/preset-env "6-job_processor.js"

[nodemon] 2.0.4
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `babel-node --presets @babel/preset-env 6-job_processor.js`
Sending notification to 4153518780, with message: This is the code to verify your account

Terminal 1: let’s queue a new job!

bob@dylan:~$ npm run dev 6-job_creator.js 

> queuing_system_in_js@1.0.0 dev /root
> nodemon --exec babel-node --presets @babel/preset-env "6-job_creator.js"

[nodemon] 2.0.4
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `babel-node --presets @babel/preset-env 6-job_creator.js`
Notification job created: 2

And in the same time in Terminal 2:

Sending notification to 4153518780, with message: This is the code to verify your account
BOOM! same as 5-subscriber.js and 5-publisher.js but with a module to manage jobs.

BOOM ! comme 5-subscriber.js et 5-publisher.js mais avec un module pour gérer les travaux.


Repo:

GitHub repository: alx-backend
Directory: 0x03-queuing_system_in_js
File: 6-job_processor.js
  
8. Track progress and errors with Kue: Create the Job creator
mandatory
In a file named 7-job_creator.js:

Create an array jobs with the following data inside:

const jobs = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account'
  },
  {
    phoneNumber: '4153518781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153518743',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153538781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153118782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4159518782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4158718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153818782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4154318781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4151218782',
    message: 'This is the code 4321 to verify your account'
  }
];
After this array created:

Create a queue with Kue
Write a loop that will go through the array jobs and for each object:
Create a new job to the queue push_notification_code_2 with the current object
If there is no error, log to the console Notification job created: JOB_ID
On the job completion, log to the console Notification job JOB_ID completed
On the job failure, log to the console Notification job JOB_ID failed: ERROR
On the job progress, log to the console Notification job JOB_ID PERCENTAGE% complete


Après la création de ce tableau :

Créer une file d'attente avec Kue
Ecrire une boucle qui va parcourir le tableau des jobs et pour chaque objet :
Créer un nouveau job dans la file d'attente push_notification_code_2 avec l'objet courant
S'il n'y a pas d'erreur, loguer dans la console Notification job created : JOB_ID
Lorsque le travail est terminé, la console affiche le journal Notification job JOB_ID completed (travail de notification terminé)
En cas d'échec de la tâche, la console enregistre la tâche de notification JOB_ID qui a échoué : ERROR
En cas de progression du travail, consignez dans la console le travail de notification JOB_ID PERCENTAGE% complete


Terminal 1:

bob@dylan:~$ npm run dev 7-job_creator.js 

> queuing_system_in_js@1.0.0 dev /root
> nodemon --exec babel-node --presets @babel/preset-env "7-job_creator.js"

[nodemon] 2.0.4
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `babel-node --presets @babel/preset-env 7-job_creator.js`
Notification job created: 39
Notification job created: 40
Notification job created: 41
Notification job created: 42
Notification job created: 43
Notification job created: 44
Notification job created: 45
Notification job created: 46
Notification job created: 47
Notification job created: 48
Notification job created: 49

Repo:

GitHub repository: alx-backend
Directory: 0x03-queuing_system_in_js
File: 7-job_creator.js
  
9. Track progress and errors with Kue: Create the Job processor
mandatory
In a file named 7-job_processor.js:

Create an array that will contain the blacklisted phone numbers. Add in it 4153518780 and 4153518781 - these 2 numbers will be blacklisted by our jobs processor.

Create a function sendNotification that takes 4 arguments: phoneNumber, message, job, and done:

When the function is called, track the progress of the job of 0 out of 100
If phoneNumber is included in the “blacklisted array”, fail the job with an Error object and the message: Phone number PHONE_NUMBER is blacklisted
Otherwise:
Track the progress to 50%
Log to the console Sending notification to PHONE_NUMBER, with message: MESSAGE
Create a queue with Kue that will proceed job of the queue push_notification_code_2 with two jobs at a time.

Requirements:

You only need one Redis server to execute the program
You will need to have two node processes to run each script at the same time
You muse use Kue to set up the queue
Executing the jobs list should log to the console the following:

Dans un fichier nommé 7-job_processor.js :

Créez un tableau qui contiendra les numéros de téléphone sur liste noire. Ajoutez-y 4153518780 et 4153518781 - ces deux numéros seront mis sur liste noire par notre processeur d'emplois.

Créez une fonction sendNotification qui prend 4 arguments : phoneNumber, message, job, et done :

Lorsque la fonction est appelée, la progression du travail est de 0 sur 100.
Si le numéro de téléphone figure dans le "tableau de listes noires", le travail échoue avec un objet Error et le message suivant : Le numéro de téléphone PHONE_NUMBER est sur liste noire.
Dans le cas contraire :
Suivre la progression jusqu'à 50 %.
Enregistrer dans la console Envoi d'une notification à PHONE_NUMBER, avec le message : MESSAGE
Créer une file d'attente avec Kue qui traitera les travaux de la file d'attente push_notification_code_2 avec deux travaux à la fois.

Exigences :

Vous n'avez besoin que d'un seul serveur Redis pour exécuter le programme
Vous aurez besoin de deux processus de nœuds pour exécuter chaque script en même temps.
Vous pouvez utiliser Kue pour mettre en place la file d'attente.
L'exécution de la liste des tâches devrait permettre d'afficher sur la console le message suivant :


Terminal 2:

bob@dylan:~$ npm run dev 7-job_processor.js 

> queuing_system_in_js@1.0.0 dev /root
> nodemon --exec babel-node --presets @babel/preset-env "7-job_processor.js"

[nodemon] 2.0.4
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `babel-node --presets @babel/preset-env 7-job_processor.js`
Sending notification to 4153518743, with message: This is the code 4321 to verify your account
Sending notification to 4153538781, with message: This is the code 4562 to verify your account
Sending notification to 4153118782, with message: This is the code 4321 to verify your account
Sending notification to 4153718781, with message: This is the code 4562 to verify your account
Sending notification to 4159518782, with message: This is the code 4321 to verify your account
Sending notification to 4158718781, with message: This is the code 4562 to verify your account
Sending notification to 4153818782, with message: This is the code 4321 to verify your account
Sending notification to 4154318781, with message: This is the code 4562 to verify your account
Sending notification to 4151218782, with message: This is the code 4321 to verify your account

And in the same time in terminal 1:

...
Notification job #39 0% complete
Notification job #40 0% complete
Notification job #39 failed: Phone number 4153518780 is blacklisted
Notification job #40 failed: Phone number 4153518781 is blacklisted
Notification job #41 0% complete
Notification job #41 50% complete
Notification job #42 0% complete
Notification job #42 50% complete
Notification job #41 completed
Notification job #42 completed
Notification job #43 0% complete
Notification job #43 50% complete
Notification job #44 0% complete
Notification job #44 50% complete
Notification job #43 completed
Notification job #44 completed
Notification job #45 0% complete
Notification job #45 50% complete
Notification job #46 0% complete
Notification job #46 50% complete
Notification job #45 completed
Notification job #46 completed
Notification job #47 0% complete
Notification job #47 50% complete
Notification job #48 0% complete
Notification job #48 50% complete
Notification job #47 completed
Notification job #48 completed
Notification job #49 0% complete
Notification job #49 50% complete
Notification job #49 completed
Repo:

GitHub repository: alx-backend
Directory: 0x03-queuing_system_in_js
File: 7-job_processor.js
  
10. Writing the job creation function
mandatory
In a file named 8-job.js, create a function named createPushNotificationsJobs:

It takes into argument jobs (array of objects), and queue (Kue queue)
If jobs is not an array, it should throw an Error with message: Jobs is not an array
For each job in jobs, create a job in the queue push_notification_code_3
When a job is created, it should log to the console Notification job created: JOB_ID
When a job is complete, it should log to the console Notification job JOB_ID completed
When a job is failed, it should log to the console Notification job JOB_ID failed: ERROR
When a job is making progress, it should log to the console Notification job JOB_ID PERCENT% complete


Dans un fichier nommé 8-job.js, créez une fonction nommée createPushNotificationsJobs :

Elle prend en argument jobs (tableau d'objets), et queue (queue Kue)
Si jobs n'est pas un tableau, la fonction doit générer une erreur avec le message : Jobs n'est pas un tableau
Pour chaque job dans jobs, créer un job dans la file d'attente push_notification_code_3
Lorsqu'un job est créé, il doit être enregistré dans la console Notification job created : JOB_ID
Lorsqu'un travail est terminé, il doit être signalé à la console Notification job JOB_ID completed
Lorsqu'un travail échoue, il doit être consigné dans la console Notification job JOB_ID failed : ERROR
Lorsqu'un travail progresse, il doit être consigné dans la console Notification job JOB_ID PERCENT% complete


bob@dylan:~$ cat 8-job-main.js 
import kue from 'kue';

import createPushNotificationsJobs from './8-job.js';

const queue = kue.createQueue();

const list = [
    {
        phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account'
    }
];
createPushNotificationsJobs(list, queue);

bob@dylan:~$
bob@dylan:~$ npm run dev 8-job-main.js 

> queuing_system_in_js@1.0.0 dev /root
> nodemon --exec babel-node --presets @babel/preset-env "8-job-main.js"

[nodemon] 2.0.4
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `babel-node --presets @babel/preset-env 8-job-main.js`
Notification job created: 51

Repo:

GitHub repository: alx-backend
Directory: 0x03-queuing_system_in_js
File: 8-job.js
  
11. Writing the test for job creation
mandatory
Now that you created a job creator, let’s add tests:

Import the function createPushNotificationsJobs
Create a queue with Kue
Write a test suite for the createPushNotificationsJobs function:
Use queue.testMode to validate which jobs are inside the queue
etc.
Requirements:

Make sure to enter the test mode without processing the jobs before executing the tests
Make sure to clear the queue and exit the test mode after executing the tests


Maintenant que vous avez créé un créateur d'emploi, ajoutons des tests :

Importer la fonction createPushNotificationsJobs
Créer une file d'attente avec Kue
Ecrire une suite de tests pour la fonction createPushNotificationsJobs :
Utiliser queue.testMode pour valider quels travaux sont dans la file d'attente
etc.
Exigences :

Assurez-vous d'entrer dans le mode de test sans traiter les travaux avant d'exécuter les tests.
Assurez-vous de vider la file d'attente et de quitter le mode test après avoir exécuté les tests.


bob@dylan:~$ npm test 8-job.test.js 

> queuing_system_in_js@1.0.0 test /root
> mocha --require @babel/register --exit "8-job.test.js"



  createPushNotificationsJobs
    ✓ display a error message if jobs is not an array
Notification job created: 1
Notification job created: 2
    ✓ create two new jobs to the queue
...

  123 passing (417ms)

Repo:

GitHub repository: alx-backend
Directory: 0x03-queuing_system_in_js
File: 8-job.test.js
 
12. In stock?
mandatory
Data
Create an array listProducts containing the list of the following products:

Id: 1, name: Suitcase 250, price: 50, stock: 4
Id: 2, name: Suitcase 450, price: 100, stock: 10
Id: 3, name: Suitcase 650, price: 350, stock: 2
Id: 4, name: Suitcase 1050, price: 550, stock: 5
Data access
Create a function named getItemById:

It will take id as argument
It will return the item from listProducts with the same id
Server
Create an express server listening on the port 1245. (You will start it via: npm run dev 9-stock.js)

Products
Create the route GET /list_products that will return the list of every available product with the following JSON format:

bob@dylan:~$ curl localhost:1245/list_products ; echo ""
[{"itemId":1,"itemName":"Suitcase 250","price":50,"initialAvailableQuantity":4},{"itemId":2,"itemName":"Suitcase 450","price":100,"initialAvailableQuantity":10},{"itemId":3,"itemName":"Suitcase 650","price":350,"initialAvailableQuantity":2},{"itemId":4,"itemName":"Suitcase 1050","price":550,"initialAvailableQuantity":5}]
bob@dylan:~$ 
In stock in Redis
Create a client to connect to the Redis server:

Write a function reserveStockById that will take itemId and stock as arguments:
It will set in Redis the stock for the key item.ITEM_ID
Write an async function getCurrentReservedStockById, that will take itemId as an argument:
It will return the reserved stock for a specific item
Product detail
Create the route GET /list_products/:itemId, that will return the current product and the current available stock (by using getCurrentReservedStockById) with the following JSON format:

bob@dylan:~$ curl localhost:1245/list_products/1 ; echo ""
{"itemId":1,"itemName":"Suitcase 250","price":50,"initialAvailableQuantity":4,"currentQuantity":4}
bob@dylan:~$ 
If the item does not exist, it should return:

bob@dylan:~$ curl localhost:1245/list_products/12 ; echo ""
{"status":"Product not found"}
bob@dylan:~$ 
Reserve a product
Create the route GET /reserve_product/:itemId:

If the item does not exist, it should return:
bob@dylan:~$ curl localhost:1245/reserve_product/12 ; echo ""
{"status":"Product not found"}
bob@dylan:~$ 
If the item exists, it should check that there is at least one stock available. If not it should return:
bob@dylan:~$ curl localhost:1245/reserve_product/1 ; echo ""
{"status":"Not enough stock available","itemId":1}
bob@dylan:~$ 
If there is enough stock available, it should reserve one item (by using reserveStockById), and return:
bob@dylan:~$ curl localhost:1245/reserve_product/1 ; echo ""
{"status":"Reservation confirmed","itemId":1}
bob@dylan:~$ 
Requirements:

Make sure to use promisify with Redis
Make sure to use the await/async keyword to get the value from Redis
Make sure the format returned by the web application is always JSON and not text


Créer un client pour se connecter au serveur Redis :

Écrire une fonction reserveStockById qui prendra itemId et stock comme arguments :
Elle définira dans Redis le stock pour la clé item.ITEM_ID
Écrire une fonction asynchrone getCurrentReservedStockById, qui prendra itemId comme argument :
Elle renverra le stock réservé pour un article spécifique.
Détail du produit
Créer la route GET /list_products/:itemId, qui renverra le produit actuel et le stock disponible actuel (en utilisant getCurrentReservedStockById) avec le format JSON suivant :

bob@dylan:~$ curl localhost:1245/list_products/1 ; echo ""
{"itemId":1, "itemName" : "Valise 250", "price":50, "initialAvailableQuantity":4, "currentQuantity":4}
bob@dylan:~$
Si l'article n'existe pas, il doit renvoyer la réponse :

bob@dylan:~$ curl localhost:1245/list_products/12 ; echo ""
{"status" : "Produit non trouvé"}
bob@dylan:~$
Réserver un produit
Créez la route GET /reserve_product/:itemId :

Si l'article n'existe pas, elle doit renvoyer :
bob@dylan:~$ curl localhost:1245/reserve_product/12 ; echo ""
{"status" : "Produit non trouvé"}
bob@dylan:~$
Si l'article existe, il doit vérifier qu'il y a au moins un stock disponible. Si ce n'est pas le cas, il doit retourner :
bob@dylan:~$ curl localhost:1245/reserve_product/1 ; echo ""
{"status" : "Pas assez de stock disponible", "itemId":1}
bob@dylan:~$
Si le stock disponible est suffisant, il doit réserver un article (en utilisant reserveStockById), et retourner :
bob@dylan:~$ curl localhost:1245/reserve_product/1 ; echo ""
{"status" : "Réservation confirmée", "itemId":1}
bob@dylan:~$
Exigences :

Assurez-vous d'utiliser promisify avec Redis
Assurez-vous d'utiliser le mot-clé await/async pour obtenir la valeur de Redis.
S'assurer que le format retourné par l'application web est toujours JSON et non pas textuel


Repo:

GitHub repository: alx-backend
Directory: 0x03-queuing_system_in_js
File: 9-stock.js
 
13. Can I have a seat?
#advanced
Redis
Create a Redic client:

Create a function reserveSeat, that will take into argument number, and set the key available_seats with the number
Create a function getCurrentAvailableSeats, it will return the current number of available seats (by using promisify for Redis)
When launching the application, set the number of available to 50
Initialize the boolean reservationEnabled to true - it will be turn to false when no seat will be available
Kue queue
Create a Kue queue

Server
Create an express server listening on the port 1245. (You will start it via: npm run dev 100-seat.js)

Add the route GET /available_seats that returns the number of seat available:

bob@dylan:~$ curl localhost:1245/available_seats ; echo ""
{"numberOfAvailableSeats":"50"}
bob@dylan:~$ 
Add the route GET /reserve_seat that:

Returns { "status": "Reservation are blocked" } if reservationEnabled is false
Creates and queues a job in the queue reserve_seat:
Save the job and return:
{ "status": "Reservation in process" } if no error
Otherwise: { "status": "Reservation failed" }
When the job is completed, print in the console: Seat reservation job JOB_ID completed
When the job failed, print in the console: Seat reservation job JOB_ID failed: ERROR_MESSAGE
bob@dylan:~$ curl localhost:1245/reserve_seat ; echo ""
{"status":"Reservation in process"}
bob@dylan:~$ 
Add the route GET /process that:

Returns { "status": "Queue processing" } just after:
Process the queue reserve_seat (async):
Decrease the number of seat available by using getCurrentAvailableSeats and reserveSeat
If the new number of available seats is equal to 0, set reservationEnabled to false
If the new number of available seats is more or equal than 0, the job is successful
Otherwise, fail the job with an Error with the message Not enough seats available
bob@dylan:~$ curl localhost:1245/process ; echo ""
{"status":"Queue processing"}
bob@dylan:~$ 
bob@dylan:~$ curl localhost:1245/available_seats ; echo ""
{"numberOfAvailableSeats":"49"}
bob@dylan:~$ 
and in the server terminal:

Seat reservation job 52 completed
and you can reserve all seats:

bob@dylan:~$ for n in {1..50}; do curl localhost:1245/reserve_seat ; echo ""; done
{"status":"Reservation in process"}
{"status":"Reservation in process"}
...
{"status":"Reservation in process"}
{"status":"Reservation in process"}
{"status":"Reservation in process"}
{"status":"Reservation are blocked"}
{"status":"Reservation are blocked"}
{"status":"Reservation are blocked"}
bob@dylan:~$ 
Requirements:

Make sure to use promisify with Redis
Make sure to use the await/async keyword to get the value from Redis
Make sure the format returned by the web application is always JSON and not text
Make sure that only the allowed amount of seats can be reserved
Make sure that the main route is displaying the right number of seats

Redis
Créer un client Redis :

Créer une fonction reserveSeat, qui prendra en argument le nombre, et définira la clé available_seats avec le nombre.
Créer une fonction getCurrentAvailableSeats, qui renverra le nombre actuel de sièges disponibles (en utilisant promisify pour Redis)
Au lancement de l'application, fixer le nombre de sièges disponibles à 50
Initialiser le booléen reservationEnabled à true - il sera transformé en false lorsqu'aucune place ne sera disponible.
File d'attente Kue
Créer une file d'attente Kue

Serveur
Créer un serveur express écoutant sur le port 1245. (Vous le démarrerez via : npm run dev 100-seat.js)

Ajouter la route GET /available_seats qui renvoie le nombre de sièges disponibles :

bob@dylan:~$ curl localhost:1245/available_seats ; echo ""
{"numberOfAvailableSeats" : "50"}
bob@dylan:~$
Ajoutez la route GET /reserve_seat qui :

renvoie { "status" : "Reservation are blocked" } si reservationEnabled est false
Crée et met en file d'attente un travail dans la file d'attente reserve_seat :
Sauvegarde le travail et renvoie { "status" : "Reservation are blocked" } si reservationEnabled est false :
{ "status" : "Reservation in process" } s'il n'y a pas d'erreur
sinon : { "status" : "Reservation failed" }
Lorsque la tâche est terminée, elle est imprimée dans la console : Le travail de réservation de siège JOB_ID est terminé
Lorsque la tâche a échoué, la console affiche : "Seat reservation job JOB_ID failed :": Le travail de réservation de siège JOB_ID a échoué : ERROR_MESSAGE
bob@dylan:~$ curl localhost:1245/reserve_seat ; echo ""
{"status" : "Réservation en cours"}
bob@dylan:~$
Ajoutez la route GET /process qui :

renvoie {"status" : "Queue processing" } juste après :
Traiter la file d'attente reserve_seat (async) :
Diminue le nombre de sièges disponibles en utilisant getCurrentAvailableSeats et reserveSeat
Si le nouveau nombre de sièges disponibles est égal à 0, la valeur de reservationEnabled est fixée à false.
Si le nouveau nombre de sièges disponibles est supérieur ou égal à 0, la tâche est réussie.
Dans le cas contraire, le job échoue avec un message d'erreur indiquant qu'il n'y a pas assez de sièges disponibles.
bob@dylan:~$ curl localhost:1245/process ; echo ""
{"status" : "Queue processing"}
bob@dylan:~$
bob@dylan:~$ curl localhost:1245/available_seats ; echo ""
{"numberOfAvailableSeats" : "49"}
bob@dylan:~$
et dans le terminal du serveur :

Seat reservation job 52 completed
et vous pouvez réserver tous les sièges :

bob@dylan:~$ for n in {1..50} ; do curl localhost:1245/reserve_seat ; echo "" ; done
{"status" : "Réservation en cours"}
{"status" : "Réservation en cours"}
...
{"status" : "Réservation en cours"}
{"status" : "Réservation en cours"} {"status" : "Réservation en cours"}
{"statut" : "Réservation en cours"} {"statut" : "Réservation en cours"}
{"status" : "Les réservations sont bloquées"}
{"statut" : "Les réservations sont bloquées"} {"statut" : "Les réservations sont bloquées"}
{"status" : "Les réservations sont bloquées"} {"status" : "Les réservations sont bloquées"}
bob@dylan:~$
Exigences :

Assurez-vous d'utiliser promisify avec Redis
Assurez-vous d'utiliser le mot-clé await/async pour obtenir la valeur de Redis.
S'assurer que le format retourné par l'application web est toujours JSON et non du texte
Assurez-vous que seul le nombre de sièges autorisé peut être réservé.
Assurez-vous que la route principale affiche le bon nombre de sièges.
Repo:

GitHub repository: alx-backend
Directory: 0x03-queuing_system_in_js
File: 100-seat.js
  
Copyright © 2023 ALX, All rights reserved.