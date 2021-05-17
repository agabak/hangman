using Catalog.API.Entities;
using Microsoft.Extensions.Configuration;
using MongoDB.Driver;
using System.Threading.Tasks;

namespace Catalog.API.Data
{
    public class CatalogContext : ICatalogContext
    {
        public CatalogContext(IConfiguration configuration)
        {
            var client = new MongoClient(configuration.GetValue<string>("DatabaseSettings:ConnectionString"));
            var databse = client.GetDatabase(configuration.GetValue<string>("DatabaseSettings:DatabaseName"));

            Products = databse.GetCollection<Product>(configuration.GetValue<string>("DatabaseSettings:CollectionName"));

           Task.Run(() => CatalogContextSeed.Seed(Products));
        }
        public IMongoCollection<Product> Products { get; }
    }
}
