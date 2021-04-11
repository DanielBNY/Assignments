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
        static void Main(string[] args)
        {
            
        }
    }
}
