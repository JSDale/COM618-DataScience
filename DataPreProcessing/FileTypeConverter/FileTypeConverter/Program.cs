
namespace FileTypeConverter
{
    using System;
    using System.Data;
    using System.IO;

    using LumenWorks.Framework.IO.Csv;

    /// <summary>
    /// Main entry for app.
    /// </summary>
    public class Program
    {
        /// <summary>
        /// Main entry for app.
        /// </summary>
        /// <param name="args">The command line args</param>
        public static void Main(string[] args)
        {
            Console.WriteLine("Enter filepath of csv. Include .csv");
            var csvFilepath = Console.ReadLine();

            var table = ReadCsv(csvFilepath);
            var dateColumn = table.Columns[0].ToString();
            Console.WriteLine(dateColumn);

            Console.WriteLine("Enter folder path to save JSON");
            var jsonFilepath = Console.ReadLine();

        }

        /// <summary>
        /// Reads the CSV.
        /// </summary>
        /// <param name="filepath">The filepath of the CSV.</param>
        /// <returns>The loaded csv table.</returns>
        public static DataTable ReadCsv(string filepath)
        {
            var csvTable = new DataTable();
            using (var csvReader = new CsvReader(new StreamReader(System.IO.File.OpenRead(filepath)), true))
            {
                csvTable.Load(csvReader);
                return csvTable;
            }
        }
    }
}
