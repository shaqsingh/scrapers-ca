from pupa.scrape import Jurisdiction

from montreal import MontrealPersonScraper
from utils import lxmlize

class Sud_Ouest(Jurisdiction):
  jurisdiction_id = 'ca-qc-sud-ouest'

  def get_metadata(self):
    return {
      'name': 'Le Sud-Ouest',
      'legislature_name': 'Sud-Ouest Borough Council',
      'legislature_url': 'http://depot.ville.montreal.qc.ca/bd-elus/data.json',
      'terms': [{
        'name': 'N/A',
        'sessions': ['N/A'],
      }],
      'provides': ['people'],
      'session_details': {
        'N/A': {
          '_scraped_name': 'N/A',
        }
      },
    }

  def get_scraper(self, term, session, scraper_type):
    if scraper_type == 'people':
        return MontrealPersonScraper

  def scrape_session_list(self):
    return ['N/A']
    