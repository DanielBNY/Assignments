using System.IO;

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

        static void Main(string[] args)
        {
            
        }
    }
}
