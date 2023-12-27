
import logging, pytz, datetime, pandas
from odoo import api, fields, models

_logger = logging.getLogger(__name__)

# Test
def test_with_logger(data: any="Debug Message", warn: bool = False) -> None:
    """
        Outputs a debug message in the odoo log file, 5 times in a row
    """
    method = _logger.info if not warn else _logger.warning
    for _ in range(5):
        method(data)

class ClockTimeZone(models.Model):
    _name = 'clock.time.zone'
    _description = 'Clock\'s Time Zone'

    timezone = fields.Char('Time Zone', required=True)
    country = fields.Char('Country')
    valid = fields.Boolean('Valid')
    by_user = fields.Many2one('res.users', string="By User")

    @api.model
    def create(self, kwargs: dict):
        """ Overrides the create method of the model """

        # Get timezone
        tz: str = str(kwargs.get('timezone', '')).strip()
        kwargs['valid'] = tz and tz in pytz.all_timezones_set
        
        # Test pandas
        test_with_logger()
        test_with_logger(pandas.array([1,2,3,4,5,6,7,8,9,0]), warn=True)

        # Check time
        try:
            timezone: datetime.tzinfo = pytz.timezone(tz)
            date_time: datetime.datetime = datetime.datetime.now()
            date_time = timezone.localize(date_time)
            date_time = date_time.strftime('%d/%m/%Y, %H:%M:%S')
            _logger.info(date_time)
        except pytz.UnknownTimeZoneError:
            _logger.warning(f'Unkown Time Zone: {tz}')

        # Save
        return super(ClockTimeZone, self).create(kwargs)