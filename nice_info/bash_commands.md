docker ps -a -q | grep -v -e 64e4d09e1015 -e d43118a0213c -e 385f2b8bee84 -e 422a9e179fa1 | xargs docker rm
(удалить все контейнеры кроме выделенных)
