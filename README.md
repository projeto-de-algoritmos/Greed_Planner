# Greed_Planner

Temas:
 - Greed

# Planner
  
**Número da Lista**: 14<br>
**Conteúdo da Disciplina**: Interval Scheduling <br>

## Alunos
|Matrícula | Aluno |
| -- | -- |
| 16/0119553  |  👨‍💻 Felipe Campos de Almeida |
| 16/0005736  |  👩‍💻 Fabiana Luiza Vasconcelos Pfeilsticker Ribas |

## Sobre ℹ️
O Planner utiliza o algoritimo de Interval Scheduling para priorizar um conjunto com maior quantidade de tarefas. No Planner é possivel adicionar tarefas e receber um conjunto que seja mais produtivo, neste caso que contenha o maior numero de tarefas a serem realizadas.

## Video
[Link para o video explicativo]()

## 📷 Screenshots 
Retorno da execução do projeto. Planner com a maior quantidade de tarefas a serem executadas.

![Planne completo]()

Retorno da execução do projeto. Adição de tasks no Planner.

![Adição de tasks /POST]()

Retorno da execução do projeto. Visualização das tasks no Planner sem a execução do Interval Scheduling.

![Tasks /GET]()

## ⚙️ Instalação 
**Linguagem**: 🐍 Python<br>
**Framework**: 💜 Insomnia<br>


### Para distribuição Linux 🐧 :

**Para a execução do projeto é necessário a instalação previa do docker e docker-compose.**

1) [Clone](https://help.github.com/en/articles/cloning-a-repository) o repositório do projeto. Para clonar vá ao terminal e digite:
~~~
$ git clone git@github.com:projeto-de-algoritmos/Greed_Planner.git
~~~

2) Entre na pasta do projeto:
~~~
$ cd Greed_Planner
~~~

3) Para compilar o projeto, execute o comando do docker:
~~~
$ docker-compose up --build
~~~

4) Depois de realizar todos esses passos, aproveite o projeto e divirta-se!

## 💻 Uso 
Utilize o isominia para as requisições http. Siga o exemplo a baixo pra utilizar a rota. Adicione suas tarefas para testar a aplicação.😉

1) Visualize a lista de tarefas existentes: http://0.0.0.0:8000/tasks
2) Adicione sua tarefa em: http://0.0.0.0:8000/task
~~~
{ 

}
~~~
3) Visualize o planner mais produtivo para a execução das suas atividades: http://0.0.0.0:8000/best_strategy

## Outros 