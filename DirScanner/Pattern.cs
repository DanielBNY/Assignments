namespace DirScanner
{
    public enum PatternType
    {
        FileName,
        FileExtension,
        FileSize
    }

    public class Pattern
    {
        public PatternType Type { get; }

        public string Value { get; }

        public Pattern(PatternType type, string value)
        {
            Type = type;
            Value = value;
        }
    }


}
