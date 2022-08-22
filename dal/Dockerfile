FROM 	alpine:3.10
RUN 	apk add --update sqlite

RUN 	mkdir /sqllitedb
WORKDIR /sqllitedb

VOLUME [ "src/prototype/dal/data" ]
ENTRYPOINT ["sqlite3"]
CMD ["bot.db"]