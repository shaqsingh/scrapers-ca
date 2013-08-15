from pupa.scrape import Jurisdiction

from .people import BrantfordPersonScraper
from utils import lxmlize

class Brantford(Jurisdiction):
  jurisdiction_id = 'ca-on-brantford'
  geographic_code = 3529006

  def get_metadata(self):
    return {
      'name': 'Brantford',
      'legislature_name': 'Brantford City Council',
      'legislature_url': 'http://cms.burlington.ca/Page110.aspx',
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
        return BrantfordPersonScraper

  def scrape_session_list(self):
    return ['N/A']
    