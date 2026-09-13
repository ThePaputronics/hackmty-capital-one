import React from 'react';
import { theme } from '../theme';

interface MetricCounterProps {
  label: string;
  value: string | number;
  sublabel?: string;
  highlight?: boolean;
}

export const MetricCounter: React.FC<MetricCounterProps> = ({
  label,
  value,
  sublabel,
  highlight = false,
}) => {
  return (
    <div
      style={{
        backgroundColor: theme.colors.card,
        border: `1px solid ${highlight ? theme.colors.accent : theme.colors.cardBorder}`,
        borderRadius: '12px',
        padding: '24px 28px',
        display: 'flex',
        flexDirection: 'column',
        boxShadow: highlight ? `0 0 24px rgba(216, 155, 66, 0.2)` : 'none',
      }}
    >
      <span
        style={{
          color: theme.colors.textMuted,
          fontFamily: theme.fonts.sans,
          fontSize: '14px',
          fontWeight: 600,
          letterSpacing: '1px',
          textTransform: 'uppercase',
          marginBottom: '10px',
        }}
      >
        {label}
      </span>
      <span
        style={{
          color: highlight ? theme.colors.accentLight : theme.colors.textPrimary,
          fontFamily: theme.fonts.mono,
          fontSize: '44px',
          fontWeight: 700,
          lineHeight: 1.1,
          letterSpacing: '-1px',
        }}
      >
        {value}
      </span>
      {sublabel && (
        <span
          style={{
            color: theme.colors.textSecondary,
            fontFamily: theme.fonts.sans,
            fontSize: '14px',
            marginTop: '8px',
          }}
        >
          {sublabel}
        </span>
      )}
    </div>
  );
};
