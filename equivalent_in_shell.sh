#!/bin/sh
function get_todo() {
  response=$(curl --write-out "HTTPSTATUS:%{http_code}" -s "$1/todos/$2")
  body=$(echo $response | sed -e 's/HTTPSTATUS\:.*//g')
  status=$(echo $response | tr -d '\n' | sed -e 's/.*HTTPSTATUS://')

  if [ ! $status -eq 200  ]; then
    echo "get_todo returned status: $status"
    exit 1
  fi

  title=$(echo $body | grep -o '"title": "[^"]*' | grep -o '[^"]*$')
  echo "Todo Title:"
  echo $title
}

get_todo "https://jsonplaceholder.typicode.com" $1