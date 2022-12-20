This codes finds the item type that appears in both compartments of each rucksack(list of items)in the given input file and provides the output of the sum of the priorities of those item types.
 
 #to process new input file, copy the new input file path in the docker file and change the CMD like below.
    
        COPY input_file.txt ./
  
        CMD ["poetry", "run", "python", "app.py", "input_file.txt"]
 
    
Follow the below steps to run the application

1.to build the docker image
    
    docker-compose build
2.to run the docker image
    
    docker-compose up
To stop or exit the application
    
    docker-compose down
