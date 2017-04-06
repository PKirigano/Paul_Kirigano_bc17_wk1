#!/usr/bin/env ruby
require 'boxr' #Box Ruby SDK

filesToUpload = ["test-1.txt","test-2.docx","test-3.pdf"] #replace with files to upload
searchQuery = "test" #replace with search query
fileType = ["txt"] #replace with file type needed
@client = Boxr::Client.new('REPLACE_WITH_YOUR_ACCESS_TOKEN') #Initialize client

def uploadfile(path_to_file)
  folder_id = 0 #Replace 0 with the folder id needed. 0 is a user's root folder
  file = @client.upload_file(path_to_file, folder_id)
  puts "Upload successful. File id: #{file.id}"
end

def searchByQuery(searchQuery)
  results = @client.search(searchQuery)
  #Print out item id for each search result
  results.each do |result|
    puts "Result found for #{searchQuery}. Match file id: #{result.id}"
  end
end

def searchByQueryAndFileType(searchQuery, fileType)
  results = @client.search(searchQuery, file_extensions: fileType)
  #Print out item id for each search result
  results.each do |result|
    puts "Result found for #{searchQuery} limited to #{fileType} file types. Match file id: #{result.id}"
  end
end

#Upload files one at a time. To optimize upload time for many files, implement parallel uploading.
filesToUpload.each do |i|
 uploadfile(i)
end

#Files uploaded to Box take 10 minutes to be reflected in the search results
searchByQuery(searchQuery) #Search for files by search query
searchByQueryAndFileType(searchQuery, fileType) #Search for files by search query limiting results to specific file types

#Successful Result
#Upload successful. File id: 000000000000
#Upload successful. File id: 000000000001
#Upload successful. File id: 000000000010
#Result found for test. Match file id: 000000000000
#Result found for test. Match file id: 000000000001
#Result found for test. Match file id: 000000000010
#Result found for test limited to ["txt"] file types. Match file id: 000000000000