
namespace FileTypeConverter
{
    using System.Collections.Generic;

    /// <summary>
    /// DTO for converting CSV to JSON.
    /// </summary>
    public class DeathsPerMonthPerLocationDto
    {
        /// <summary>
        /// Gets or sets the date to store.
        /// </summary>
        public string Date { get; set; }

        /// <summary>
        /// Gets or sets the deaths per location to store.
        /// </summary>
        public Dictionary<string, int> DeathByLocation { get; set; }
    }
}
