from pupa.scrape import Jurisdiction

from .people import SaskatchewanPersonScraper
from utils import lxmlize

class Saskatchewan(Jurisdiction):
  jurisdiction_id = 'ca-sk'
  geographic_code = 47
  def get_metadata(self):
    return {
      'name': 'Saskatchewan',
      'legislature_name': 'Saskatchewan City Council',
      'legislature_url': 'http://www.municipal.gov.sk.ca/Programs-Services/Municipal-Directory-pdf',
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
        return SaskatchewanPersonScraper

  def scrape_session_list(self):
    return ['N/A']
    