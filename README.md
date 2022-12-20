 Finding the item type that appears in both compartments of each rucksack(list of items)in the given input file. application provides  the sum of the priorities of those item types.
 
 #to process new input file, copy the new input file path in the docker file.
    
        COPY input_file.txt ./
  
        CMD ["poetry", "run", "python", "app.py", "input_file.txt"]
 
    

--to build the docker image
    
    docker-compose build
--to run the docker image
    
    docker-compose up
--to stop the docker image 
    
    docker-compose down
