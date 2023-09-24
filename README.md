# 4bits
Ai-Ally : : Risk Assessment Chatbot for Suicide Prevention 
Introducción 
Esta es una Web-App desarrollada el 24/09/23 por Jorge Blásquez, Adolfo Hernández, Fernanda Dáaz y Miguel Barrientos, todos estudiantes del Tecnológico de Monterrey Campus GDL, desarrollamos este proyecto con el propósito principal de participar en el décimo HackMTY, enfocándonos en una problemática en común de dos de los miembos del equipo la cual tiene un peso significativo por acontesimientos del pasado.

Problemática
En una lluvia de ideas dos de los miembros tuvieron una misma idea común, enfocándose en atacar y resolver la problemática del sucidio, ya que hoy en dia no existe una medida de atención inmediata al paciente que levanta la mano y grita por ayuda, por lo que muchos de estos pacientes son puestos en listas de espera de más de 30 minutos, y más del 60% de estos terminan quitándose la vida. 

Principal Objetivo 
Poder darle al paciente o al usuario una interacción inmediata sin tiempos de espera a ser escuchado para evaluar su riesgo inmediato, mientras es conectado con un profesional de la salud mental.

Software utilizado
- Desarrollado en Streamlit
- Implementación de IA utilizando key del modelo ChatGPT-3.5
- Utilización de base de datos de Supabase
- Base de datos de keywords que limitan las preguntas a AuroraBot
- Acceso a la plataforma proporcionando un número telefónico. Est

Desarrollo 
Con esto, tomando como punto de partida el enfoque de uno de los retos del HackMTY decidimos alinear nuestro proyecto a desarrollar una inteligencia artificial que atienda en primera instancia a la persona en busca de ayuda urgente.
¿Cómo funciona esto ?
1.- El usuario en busca de ayuda entra a nuestra página web con el objetivo de ser atendido por un especialista.
2.- Si todo profesionista está ocupado, estos son puestos en una lista de espera, donde sin que ellos los sepan se evalua su nivel de riesgo y urgencia de ser atendidos, con el propósito de que los especialistas atiendan a los pacientes en orden de riesgo.
3.- Despues se redirige al paciente a ser atendido por nuestra IA Aurora, la cual se espera satisfasca momentaneamente al paciente de ser escuchado y desahogarse miesntras se le asigna un especialista lo antes posible.
4.- Si otro usuario ingresa a nuestro sitio web y es evaluado con un nivel de riesgo más alto y con mas probabilidades de cometer un acto suicida, nuestro algoritmo hace una jerarquizacion de riesgo, y este nuevo usuario obtiene una evaluación de riesgo más grave que el anterior, sera atendido con mayor antelación. 

Conclusión 
El objetivo principal del proyecto se completó, pero el alcance del proyecto a futuro es muy amplio, incluso tal vez más del que nos imaginamos al comenzar. Consideramos que es posible desarrollar he implementar una empresa privada u organización sólida, donde hagamos conexiones psicólogo-paciente, de manera virtual y presencial, con el objetivo de proporcionar a la población una ayuda de calidad a su salud mental al alcance de un su móvil.

Áreas de Mejora 
Como equipo logramos identificar algunas áreas de mejora para darle al usuario una mejor experiencia.
- Consultar psicólogos y especialistas en salud mental para diseñar correctamente la evaluación de riesgo. 
- Utilizar machine learning y ampliar la base de datos que limita los mensajes del usuario a ser relacionados con salud mental.