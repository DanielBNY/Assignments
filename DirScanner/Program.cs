using System.Collections.Generic;
using System.IO;
using Microsoft.VisualBasic.FileIO;
namespace DirScanner
{
    class Program
    {
        string PathToScan = @"C:\code\kela-interviews\Interviews\DirScanner\path_to_scan";

        Pattern[] PatternsToMatch = new Pattern[] 
        { 
            new Pattern(PatternType.FileName, "doc1.txt"),
            new Pattern(PatternType.FileName, "doc3.txt"),
            new Pattern(PatternType.FileExtension, "log")
        };
        public static bool IsMatchingPattern(FileInfo file, Pattern[] patterns)
        {
            bool isMatch = false;
            foreach (Pattern pattern in patterns)
            {
                if (pattern.Type == PatternType.FileName && file.Name == pattern.Value)
                {
                    isMatch = true;
                }
                else if (pattern.Type == PatternType.FileExtension && file.Extension == pattern.Value)
                {
                    isMatch = true;
                }
            }
            return isMatch;
        }
        public static List<FileInfo> getAllFilesInDirectory(string directoryPath)
        {
            var directoriesInDir = Directory.GetDirectories(directoryPath);
            List<FileInfo> FilesList = new List<FileInfo>();
            var filesInCurrentDir = Directory.GetFiles(directoryPath);
            foreach (string filePath in filesInCurrentDir)
            {
                var fileInfo = FileSystem.GetFileInfo(filePath)
            }
            FilesList.Add(fileInfo);
            foreach (string dirPath in directoriesInDir)
            {
                var files = getAllFilesInDirectory(dirPath);
                foreach (FileInfo file in files)
                {
                    FilesList.Add(file);
                }
            }
            return FilesList;
        }
        static void Main(string[] args)
        {
            
        }
    }
}
