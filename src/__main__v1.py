import sys
import click
from SPARQLWrapper import SPARQLWrapper, JSON
import json
from config import configuration


def get_results(endpoint_url, orcid):
    query = """select ?p ?o where {
         ?s <http://www.wikidata.org/prop/direct-normalized/P496> <"""+orcid+""">.
         ?s ?p ?o
        }"""
    sparql = SPARQLWrapper(endpoint_url)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    return sparql.query().convert()

@click.command()
@click.option('-i', '--input_orcid', type=str, required=True, help="input path of the file or directory to inspect.")
@click.option('-o', '--output_path', type=str, default="data.json",
              help="output path for our JSON file.")    
def main(input_orcid, output_path):
    # orcid = "https://orcid.org/0000-0003-0454-7145"
    results = get_results(configuration.endpoint_url, input_orcid)
    # output_path = "data.json"
    with open(output_path, 'w') as f:
        json.dump(results, f)

    print(f"All data saved in %s " % output_path) 


if __name__ == "__main__":    
    main()
    
